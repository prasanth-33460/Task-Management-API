# Backend/DevOps Skills Assessment - Task Management API

## Overview
Build a simple task management system with authentication and role-based access control in **1 day**. This test evaluates backend development skills using FastAPI and basic DevOps capabilities.

## Test Scope: Task Management API

### Core Requirements

#### 1. Database Design (3-4 Tables with Dependencies)

Design and implement the following database schema:

```sql
Users
├── id (PK)
├── email (unique, not null)
├── hashed_password (not null)
├── full_name
├── role (enum: 'admin', 'manager', 'user')
├── is_active (boolean, default: true)
├── created_at (timestamp)
└── updated_at (timestamp)

Projects  
├── id (PK)
├── name (not null)
├── description (text)
├── owner_id (FK → Users)
├── status (enum: 'active', 'completed', 'archived')
├── created_at (timestamp)
└── updated_at (timestamp)

Tasks
├── id (PK)
├── title (not null)
├── description (text)
├── project_id (FK → Projects)
├── assigned_to (FK → Users, nullable)
├── status (enum: 'todo', 'in_progress', 'done')
├── priority (enum: 'low', 'medium', 'high')
├── due_date (datetime, nullable)
├── created_at (timestamp)
└── updated_at (timestamp)

Task_Comments
├── id (PK)
├── task_id (FK → Tasks)
├── user_id (FK → Users)
├── comment_text (text, not null)
├── created_at (timestamp)
└── updated_at (timestamp)
```

#### 2. Backend Features

**Authentication System:**
- JWT-based user registration and login
- Password hashing (bcrypt)
- Role-based access control
- Protected route middleware

**API Endpoints:**

**Users Management:**
- `POST /auth/register` - User registration
- `POST /auth/login` - User authentication
- `GET /users/me` - Get current user profile
- `PUT /users/me` - Update user profile

**Projects Management:**
- `GET /projects` - List all projects (filtered by access)
- `POST /projects` - Create new project (managers/admins only)
- `GET /projects/{id}` - Get project details
- `PUT /projects/{id}` - Update project (owner/admin only)
- `DELETE /projects/{id}` - Delete project (owner/admin only)

**Tasks Management:**
- `GET /projects/{project_id}/tasks` - List tasks in project
- `POST /projects/{project_id}/tasks` - Create task
- `GET /tasks/{id}` - Get task details
- `PUT /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task
- `PUT /tasks/{id}/assign` - Assign task to user

**Comments:**
- `GET /tasks/{task_id}/comments` - List task comments
- `POST /tasks/{task_id}/comments` - Add comment

   #### 3. Business Logic & Authorization

   **Role Permissions:**
   - **Admin**: Full access to all resources
   - **Manager**: Can create projects, manage projects they own, assign tasks
   - **User**: Can view assigned projects, update own assigned tasks, add comments

   **Access Rules:**
   - Users can only see projects they own or are assigned tasks in
   - Only project owners and admins can delete projects
   - Task assignment requires manager role or higher
   - Users can only update tasks assigned to them
   - Comments are visible to all project members

#### 4. Technical Stack Requirements

**Backend Framework:**
- FastAPI (latest stable version)
- SQLAlchemy 2.0+ for ORM
- Pydantic for data validation
- Alembic for database migrations

**Database:**
- SQLite for simplicity (production-ready setup)
- Proper foreign key constraints
- Database indexes on frequently queried fields

**Authentication:**
- JWT tokens with expiration
- Password hashing with bcrypt
- Bearer token authentication

**Code Quality:**
- Type hints throughout
- Proper error handling with HTTP status codes
- Input validation using Pydantic models
- Clean code structure following FastAPI best practices

#### 5. DevOps Requirements

**Containerization:**
- `Dockerfile` for the application
- `docker-compose.yml` with application and database services
- Multi-stage build (optional bonus)

**Configuration:**
- Environment-based configuration using `.env`
- Separate settings for development/production
- Database connection configuration

**Database Management:**
- Alembic migration scripts
- Initial data seeding (create admin user)
- Database initialization script

**Documentation:**
- Comprehensive README.md with setup instructions
- API documentation (auto-generated OpenAPI)
- Example requests and responses

## Evaluation Criteria

### Backend Skills (70% weight)

**API Design (20%):**
- [ ] RESTful endpoint structure
- [ ] Proper HTTP methods and status codes
- [ ] Consistent response format
- [ ] Error handling and validation

**Database Design (20%):**
- [ ] Proper table relationships and foreign keys
- [ ] Appropriate data types and constraints
- [ ] Database migrations work correctly
- [ ] Indexing strategy

**Authentication & Authorization (15%):**
- [ ] JWT implementation
- [ ] Password security
- [ ] Role-based access control
- [ ] Protected routes

**Code Quality (15%):**
- [ ] Clean, readable code structure
- [ ] Proper separation of concerns
- [ ] Type hints and validation
- [ ] Error handling

### DevOps Skills (30% weight)

**Containerization (15%):**
- [ ] Working Dockerfile
- [ ] Docker-compose setup
- [ ] Container networking
- [ ] Volume management

**Configuration & Deployment (10%):**
- [ ] Environment configuration
- [ ] Database initialization
- [ ] Application startup process
- [ ] Production considerations

**Documentation (5%):**
- [ ] Clear setup instructions
- [ ] API documentation
- [ ] Troubleshooting guide
- [ ] Example usage

## Deliverables

### Required Files
1. **Source Code**
   - Complete FastAPI application
   - Database models and migrations
   - API endpoints with proper validation
   - Authentication middleware

2. **Docker Setup**
   - `Dockerfile`
   - `docker-compose.yml`
   - `.env.example` file

3. **Documentation**
   - `README.md` with comprehensive setup guide
   - API documentation (OpenAPI/Swagger)
   - Sample requests and responses

4. **Database**
   - Alembic migration files
   - Sample data seeding script
   - Database schema documentation

### Bonus Points
- Unit tests for key endpoints
- GitHub Actions workflow
- Logging implementation
- Rate limiting
- API versioning
- Health check endpoints

## Setup Instructions for Candidate

### Prerequisites
- Python 3.11+
- Docker and Docker Compose
- Git

### Getting Started
1. Clone the provided repository template
2. Create your feature branch
3. Implement the requirements
4. Test your implementation
5. Create comprehensive documentation
6. Submit via pull request or zip file

## Time Allocation Suggestions

- **Database Design & Models**: 2-3 hours
- **Authentication System**: 2-3 hours
- **Core API Endpoints**: 4-5 hours
- **Authorization Logic**: 1-2 hours
- **Docker & DevOps Setup**: 1-2 hours
- **Documentation & Testing**: 1-2 hours

**Total Estimated Time**: 8-10 hours (1 full day)

## Submission Guidelines

1. **Code Quality**: Code should be production-ready with proper error handling
2. **Git History**: Clean commit messages showing development progress
3. **Documentation**: README should allow easy setup by reviewers
4. **Testing**: Application should start successfully with `docker-compose up`
5. **Demo Data**: Include script to create sample users and projects

## Sample API Usage

```bash
# Register a user
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123","full_name":"Test User","role":"user"}'

# Login
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=password123"

# Create a project (with auth token)
curl -X POST "http://localhost:8000/projects" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Project","description":"A test project"}'
```

## Questions or Clarifications

If you have any questions during the test, please document your assumptions in the README and proceed with implementation.

Good luck! 🚀