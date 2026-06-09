import os
import json
import subprocess

# Create folders
folders = ["config", "models", "public", "views"]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
files = ["app.js", ".gitignore"]

for file in files:
    if not os.path.exists(file):
        open(file, "w").close()

# package.json content
package_json = {
    "name": os.path.basename(os.getcwd()).lower(),
    "version": "1.0.0",
    "description": "",
    "main": "app.js",
    "scripts": {
        "start": "node app.js",
        "dev": "nodemon app.js"
    },
    "keywords": [],
    "author": "",
    "license": "ISC",
    "dependencies": {
        "bcrypt": "^6.0.0",
        "cookie-parser": "^1.4.7",
        "ejs": "^3.1.10",
        "express": "^5.2.1",
        "jsonwebtoken": "^9.0.3",
        "mongoose": "^9.6.3"
    },
    "devDependencies": {
        "nodemon": "^3.1.14"
    }
}

# Write package.json
with open("package.json", "w") as f:
    json.dump(package_json, f, indent=2)

# Starter Express server
app_js = """const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send('Server is running...');
});

app.listen(8000, () => {
    console.log('Server is live on port 8000');
});
"""

with open("app.js", "w") as f:
    f.write(app_js)

print("Installing dependencies...")

try:
    subprocess.run(
        [
            "npm.cmd",
            "install",
            "bcrypt",
            "cookie-parser",
            "ejs",
            "express",
            "jsonwebtoken",
            "mongoose"
        ],
        check=True
    )

    subprocess.run(
        [
            "npm.cmd",
            "install",
            "--save-dev",
            "nodemon"
        ],
        check=True
    )

    print("\n✅ Project setup completed successfully!")
    print("👉 Run: npm run dev")

except Exception as e:
    print("\n❌ Error installing dependencies:")
    print(e)