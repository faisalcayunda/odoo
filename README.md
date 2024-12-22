# Odoo Project

This repository contains a dockerized Odoo project setup with custom addons and configurations.

## Project Structure

```
.
├── addons/         # Custom Odoo modules
├── config/         # Odoo configuration files
├── data/          # Data directory for Odoo
└── docker-compose.yml  # Docker compose configuration
```

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd odoo_project
   ```

2. Copy the example environment file and adjust as needed:
   ```bash
   cp .env.example .env
   ```

3. Start the containers:
   ```bash
   docker-compose up -d
   ```

4. Access Odoo:
   - Web Interface: http://localhost:8069
   - Master password: Check your .env file

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# PostgreSQL Configuration
POSTGRES_DB=postgres
POSTGRES_PASSWORD=odoo
POSTGRES_USER=odoo
PGDATA=/var/lib/postgresql/data/pgdata

# Odoo Configuration
HOST=postgres
USER=odoo
PASSWORD=odoo
```

### Environment Variables Description

- **PostgreSQL Configuration**:
  - `POSTGRES_DB`: Name of the PostgreSQL database
  - `POSTGRES_PASSWORD`: Password for the PostgreSQL database
  - `POSTGRES_USER`: PostgreSQL database user
  - `POSTGRES_HOST`: PostgreSQL host service name

- **Odoo Configuration**:
  - `HOST`: Database host for Odoo
  - `USER`: Database user for Odoo
  - `PASSWORD`: Database password for Odoo
  
> **Note**: For security reasons, make sure to change default passwords in production environment.

## Development

### Custom Addons
Place your custom Odoo modules in the `addons/` directory. They will be automatically detected by Odoo.

### Configuration
- Main Odoo configuration is in `config/` directory
- Environment variables are managed through `.env` file

## Maintenance

### Database Backup
```bash
docker-compose exec db pg_dump odoo > backup.sql
```

### Logs
```bash
docker-compose logs -f
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
