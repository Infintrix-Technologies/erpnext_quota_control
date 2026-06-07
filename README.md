### ERPNext Quota Control

Control ERPNext Quota From User Friendly UI

This is the control server app for **erpnext_quota**. It provides a webhook API and a form-based UI to manage tenant quota limits.

### Dependencies

This app is the control backend for **erpnext_quota** ([erpnext_quota](https://github.com/muqeetmughal/erpnext_quota)). Install erpnext_quota on each tenant site that needs quota enforcement.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench --site control.server.site install-app quota_control
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/quota_control
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.

### License

mit
