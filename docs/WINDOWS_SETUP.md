# Windows 11 Setup Guide — BookingScraper Pro v48

## Prerequisites Install Order

### 1. Visual C++ Redistributables
Download from: https://aka.ms/vs/17/release/vc_redist.x64.exe
Required for: lxml, psycopg binary wheels

### 2. Python 3.11+ x64
Download from: https://www.python.org/downloads/windows/
During install:
- ✅ Add Python to PATH
- ✅ Install for all users
- ✅ py launcher

### 3. PostgreSQL 16
Download from: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
- Choose x86-64 installer
- Note down superuser password
- Default port: 5432

### 4. Memurai (Redis for Windows)
Download from: https://www.memurai.com/
Preferred over WSL Redis for single-node desktop deployments.
Default port: 6379

### 5. NordVPN (Optional)
Only required if VPN_ENABLED=true in .env
Download from: https://nordvpn.com/download/

## Power Plan Configuration

```powershell
# Set High Performance power plan (required for production)
powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c

# Disable sleep (prevents database connections from dropping)
powercfg /change standby-timeout-ac 0
powercfg /change hibernate-timeout-ac 0
```

## Windows Defender Exclusions

```powershell
# Run PowerShell as Administrator
Add-MpPreference -ExclusionPath "C:\Program Files\PostgreSQL"
Add-MpPreference -ExclusionPath "C:\Program Files\Memurai"
Add-MpPreference -ExclusionPath "$env:USERPROFILE\BookingScraper"
Add-MpPreference -ExclusionProcess "python.exe"
Add-MpPreference -ExclusionProcess "celery.exe"
Add-MpPreference -ExclusionProcess "postgres.exe"
```

## Long Path Support

```powershell
# Enable long file paths (Windows 10 1607+ / Windows 11)
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
    -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

## PostgreSQL Configuration

Edit: `C:\Program Files\PostgreSQL\16\data\postgresql.conf`

```ini
# Connection limits (Windows Desktop Heap)
max_connections = 50

# Memory (adjust based on installed RAM)
shared_buffers = 512MB          # ~25% of RAM for 2GB system
effective_cache_size = 1536MB   # ~75% of RAM
work_mem = 8MB
maintenance_work_mem = 128MB

# WAL
wal_buffers = 16MB
checkpoint_completion_target = 0.9

# I/O (Windows)
random_page_cost = 1.1          # NVMe SSD
effective_io_concurrency = 1    # Windows async I/O limitation

# Logging
log_min_duration_statement = 1000   # ms - log slow queries
log_destination = 'eventlog'        # Windows Event Log integration
```

Edit: `C:\Program Files\PostgreSQL\16\data\pg_hba.conf`

```conf
# Local connections — trust for development, scram-sha-256 for production
local   all   all                   trust
host    all   all   127.0.0.1/32    scram-sha-256
host    all   all   ::1/128         scram-sha-256
```

## Register as Windows Service (Optional)

```batch
# Install service (run as Administrator)
cd C:\path\to\BookingScraper
.venv\Scripts\activate.bat
python windows_service.py install
python windows_service.py start

# Verify
sc query BookingScraperPro
```

## Firewall Rules

```powershell
# PostgreSQL — local only (do NOT open to network on desktop)
New-NetFirewallRule -DisplayName "PostgreSQL Local" `
    -Direction Inbound -LocalPort 5432 `
    -Protocol TCP -Action Allow `
    -RemoteAddress LocalSubnet

# API server — local only
New-NetFirewallRule -DisplayName "BookingScraper API" `
    -Direction Inbound -LocalPort 8000 `
    -Protocol TCP -Action Allow `
    -RemoteAddress LocalSubnet
```
