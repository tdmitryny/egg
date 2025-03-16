EggTracker/                      # Root directory
│
├── manage.py                    # Django's command-line utility
│
├── eggtracker/                  # Main project directory
│   ├── settings.py              # Project settings (SEO, Bootstrap config)
│   ├── urls.py                  # Main URL routing
│   └── wsgi.py                  # Web server configuration
│
├── tracking/                    # Core egg tracking functionality
│   ├── models.py                # Egg tracking data models
│   ├── views.py                # View logic for egg tracking
│   └── urls.py                 # URL patterns for tracking
│
├── blog/                       # Blog application
│   ├── models.py               # Blog post and category models
│   ├── views.py                # Blog view logic
│   └── urls.py                 # Blog URL patterns
│
├── charts/                     # Data visualization app
│   ├── models.py               # Chart data models
│   ├── views.py                # Chart generation views
│   └── urls.py                 # Chart URL patterns
│
├── maps/                       # Mapping functionality
│   ├── models.py               # Location data models
│   ├── views.py                # Map view logic
│   └── urls.py                 # Map URL patterns
│
├── templates/                  # HTML templates
│   ├── base.html              # Base template with Bootstrap
│   ├── tracking/              # Egg tracking templates
│   │   ├── dashboard.html     # Main dashboard
│   │   └── detail.html        # Detailed egg view
│   ├── blog/                  # Blog templates
│   │   ├── list.html         # Blog post list
│   │   └── detail.html       # Blog post detail
│   ├── charts/               # Chart templates
│   │   └── dashboard.html    # Charts dashboard
│   └── maps/                 # Map templates
│       └── view.html         # Map view
│
├── static/                    # Static files
│   ├── css/                  # CSS files
│   │   └── style.css        # Custom styles
│   ├── js/                  # JavaScript files
│   │   ├── charts.js       # Chart configurations
│   │   └── maps.js         # Map configurations
│   └── images/              # Image assets
│
└── media/                    # User-uploaded content
    └── blog/                # Blog post images