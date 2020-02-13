# Sample Postman collections for starmicroservices

This folder contains Postman collection files. To use them properly you need to import them into Postman and setup environment
for it.

## Importing collections
To do this just run Postman application. In top right corner you you can find Import button next to New button. Press it,
new dialog will appear. Select any file from this folder. Clicking on it will start import process.

## Collection requests
Each collection contains one request called "Smoke Test". It was created to easily check does microservice started correctly.

After sending this request you should receive response with this content:

```json
{
    "data": {
        "status": "OK"
    }
}
```

## Environments.
To use correctly this collections you need to setup new environment. You can create new one using ⚙️ button in top right
corner.

### Importing environment
In new modal select Import button at bottom of it. Select file `starmicroservices local.postman_environment.json` from this
folder.

### Create environment manually
In new modal select Add button at bottom of it. Provide your name for environment, for example 
`starmicroservices local`. Add this variables but providing the same value in both initial and current value to this names:

| Variable name   | Value             |
|-----------------|-------------------|
| protocol        | http              |
| webapp_host     | localhost:5060    |
| auth_host       | localhost:5040    |
| resource_host   | localhost:5050    |

### Selecting environment
After this select new environment in top right corner next to ⚙️ Button. Don't forget about changing that
