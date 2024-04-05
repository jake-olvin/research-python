# Hydra

[Documentation](https://hydra.cc/)

### A simple command-line application
- app/simple_app.py

In this example, Hydra creates an empty cfg object and passes it to the function annotated with @hydra.main.
You can add config values via the command line. The + indicates that the field is new.

```bash
poetry run python research/hydra-config/app/simple_app.py +db.driver=mysql +db.user=omry +db.password=secret
```