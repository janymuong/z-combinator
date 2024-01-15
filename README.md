# Z-Combinator Twttr

Z-Combinator Twttr is a Django-based app for __`typing out thoughts`__. Authenticated users can post short messages (bleeps).

## Setup

1. **GIT:**
   ```bash
   git clone https://github.com/janymuong/z-combinator-twttr.git
   cd z-combinator
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables:**
   Create a `.env` file in the project root with the content:
   ```env
   DB_NAME=mydatabase
   DB_USER=myuser
   DB_PASSWORD=mypassword
   DB_HOST=localhost
   DB_PORT=5432
   ```

4. **Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the Z-Combinator Twttr app.

## Features

- User registration and authentication
- Posting and viewing short messages (bleeps)
- Dark mode toggle
- PostgreSQL database backend
- Environment variable configuration for sensitive data

## Contributing

If you'd like to contribute to the project, feel free to submit issues or pull requests. Your contributions are welcome!

---
[MIT License](LICENSE).