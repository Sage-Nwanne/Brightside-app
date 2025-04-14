# Brightside - A Personal Reflection Journal

![Brightside Logo](main_app/static/images/Brightside-line.png)

## Description
Brightside is a digital journaling application designed to help people slow down, reflect deeply, and rediscover joy through intentional gratitude. The platform provides a safe, personal space for users to capture their thoughts, track their moods, and archive meaningful memories.

## Features
- **Personal Journaling**: Create, edit, and manage journal entries
- **Mood Tracking**: Track your emotional state with each entry
- **Archive System**: Save and organize important memories
- **Reflection Section**: Add additional thoughts and reflections to past entries
- **Secure Authentication**: Private, user-specific content

## Technologies Used
- Django 5.2
- Python 3.11
- PostgreSQL
- HTML5
- CSS3
- WhiteNoise (static files)
- Gunicorn
- Heroku (deployment)

## Getting Started
### Prerequisites
- Python 3.11+
- PostgreSQL
- Pipenv

### Installation
1. Clone the repository:
```bash
git clone <repository-url>
```

2. Install dependencies:
```bash
pipenv install
```

3. Create a `.env` file in the root directory and add:
```
SECRET_KEY=your_secret_key
```

4. Create PostgreSQL database:
```bash
createdb brightside
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## Usage
1. Create an account or log in
2. Create new journal entries from the dashboard
3. Add mood indicators to track emotional patterns
4. Review past entries in the journal view
5. Archive special memories for safekeeping
6. Add reflections to existing entries

## Project Structure
```
brightside/
├── main_app/           # Main application directory
│   ├── static/        # Static files (CSS, images)
│   ├── templates/     # HTML templates
│   ├── models.py      # Database models
│   └── views.py       # View logic
├── brightside/        # Project configuration
└── manage.py         # Django management script
```

## Authentication Features
- User registration
- Login/logout functionality
- Password validation
- Protected routes for authenticated users

## Database Schema
- **User**: Django's built-in user model
- **Entry**: Journal entries with title, content, mood, and timestamps
- **Comments**: Reflection comments linked to entries

## Deployment
The application is configured for deployment on Heroku with:
- WhiteNoise for static file serving
- Gunicorn as the production server
- PostgreSQL as the production database

## Future Enhancements
- [ ] Rich text editing
- [ ] Image attachments
- [ ] Mood analytics and insights
- [ ] Export functionality
- [ ] Mobile application

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
- Built with Django web framework
- Designed for emotional wellness and personal growth
- Inspired by the power of gratitude and self-reflection

---
*"Capture the good. Reflect with purpose. Live on the Brightside."*