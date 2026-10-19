# Tutorial / conceptual lecture — no new app code. Goal: get the
# Streamlit todo app onto a PUBLIC URL using Streamlit Community Cloud.
#
# 1. CLEAN PROJECT
#    Make a fresh PyCharm project that contains ONLY the web-app files.
#    Bring along:
#      web.py         (the Streamlit frontend)
#      functions.py   (the backend, unchanged)
#      todos.txt      (optional starter data)
#    Leave the desktop GUI and CLI files out — they're not part of the
#    deployed app.
#
# 2. SET UP A VIRTUAL ENVIRONMENT FOR THE PROJECT
#    PyCharm: tick "New environment using virtualenv" when creating
#    the project. Then install Streamlit into the new venv:
#       pip install streamlit
#    Confirm it works locally:
#       streamlit run web.py
#
# 3. CREATE requirements.txt
#    Streamlit Cloud needs to know which third-party packages to
#    install. Generate the list from the venv:
#       pip freeze > requirements.txt
#    The file looks something like:
#       streamlit==1.x.x
#       pandas==2.x.x
#       ...
#    Add it to the project root.
#
# 4. PUSH TO GITHUB
#    git init / commit / push the project to a new GitHub repo.
#    Make sure web.py, functions.py, todos.txt, and requirements.txt
#    are all committed.
#
# 5. DEPLOY ON STREAMLIT CLOUD
#    Go to https://streamlit.io/cloud, sign in with GitHub, and:
#      - Pick the repo and the branch.
#      - Set "Main file path" to `web.py`.
#      - Click Deploy. Wait a minute or two.
#    Streamlit gives you a public URL like
#       https://<your-app-name>.streamlit.app
#    that anyone can visit.
#
# 6. UPDATES
#    Push new commits to GitHub — Streamlit Cloud redeploys
#    automatically. View "Manage app" to see logs and errors.
#
# Limitations: Streamlit Cloud is free but can't be scaled up. For
# heavier traffic, see lecture 206's notes on Heroku / DigitalOcean.
