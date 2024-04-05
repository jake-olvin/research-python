# Hydra

[Documentation](https://hydra.cc/)

## A simple command-line application
- `simple/app.py`

In this example, Hydra creates an empty cfg object and passes it to the function annotated with @hydra.main.
You can add config values via the command line. The + indicates that the field is new.

```bash
poetry run python research/hydra_exs/simple/app.py +db.driver=mysql +db.user=omry +db.password=secret
```

## Specifying a config file
- `simple-config/app.py`

Specify the config name by passing a config_name parameter to the `@hydra.main()` decorator. Note that you should omit the `.yaml` extension. Hydra also needs to know where to find your config. Specify the directory containing it relative to the application by passing `config_path`.

Specify the config name by passing a `config_name` parameter to the `@hydra.main()` decorator. Note that you should omit the `.yaml` extension. Hydra also needs to know where to find your config. Specify the directory containing it relative to the application by passing `config_path`.

`simple-config/config.yaml` is loaded automatically when you run your application.

```bash
poetry run python research/hydra_exs/simple-config/app.py
```

You can override values in the loaded config from the command line.
Note the lack of the + prefix.

```bash
poetry run python research/hydra_exs/simple-config/app.py db.user=root db.password=1234
```

Use `++` to override a config value if it's already in the config, or add it otherwise.

```bash
poetry run python research/hydra_exs/simple-config/app.py ++db.password=1234 ++db.timeout=5
```

## Using the config object
- hydra-config/main.py

Here are some basic features of the Hydra Configuration Object.

```bash
poetry run python research/hydra_exs/hydra-config/main.py
```

## Grouping config files
- `group-config/app.py`

Suppose you want to benchmark your application on each of PostgreSQL and MySQL. To do this, use config groups.

A Config Group is a named group with a set of valid options. Selecting a non-existent config option generates an error message with the valid options.

### Creating config groups
To create a config group, create a directory, e.g. db, to hold a file for each database configuration option. Since we are expecting to have multiple config groups, we will proactively move all the configuration files into a conf directory.

### Using config groups
Since we moved all the configs into the conf directory, we need to tell Hydra where to find them using the `config_path` parameter. `config_path` is a directory relative to `app.py`.

Running `app.py` without requesting a configuration will print an empty config.

```bash
poetry run python research/hydra_exs/group-config/app.py
```

Select an item from a config group with +GROUP=OPTION, e.g:

```bash
poetry run python research/hydra_exs/group-config/app.py +db=postgresql
```
By default, the config group determines where the config content is placed inside the final config object. In Hydra, the path to the config content is referred to as the config package. The package of db/postgresql.yaml is db:

Like before, you can still override individual values in the resulting config:

```bash
poetry run python research/hydra_exs/group-config/app.py +db=postgresql db.timeout=20
```

## Selecting default configs
- `default-config/app.py`

After office politics, you decide that you want to use MySQL by default. You no longer want to type +db=mysql every time you run your application.

You can add a Default List to your config file. A Defaults List is a list telling Hydra how to compose the final config object. By convention, it is the first item in the config.

### Config group defaults

```yaml
defaults:
  - db: mysql
```

When you run the updated application, MySQL is loaded by default.

```bash
poetry run python research/hydra_exs/default-config/app.py
```

You can have multiple items in the defaults list, e.g.

```yaml
defaults:
  - db: mysql
  - db/mysql/engine: innodb
```

The defaults are ordered:

- If multiple configs define the same value, the last one wins.
- If multiple configs contribute to the same dictionary, the result is the combined dictionary.

### Overriding a config group default
You can still load PostgreSQL, and override individual values.

```bash
poetry run python research/hydra_exs/default-config/app.py db=postgresql db.timeout=20
```
