# Contributing

When contributing to this repository, please first discuss the change you wish
to make via issue, email, or any other method with the owners of this repository
before making a change. 

Please note we have a [code of conduct](CODE_OF_CONDUCT.md), please follow it in
all your interactions with the project.

## Getting Started

### 1. Fork and clone the repository

```bash
git clone https://github.com/guillaumegilles/guillaumegilles.github.io
cd guillaumegilles.github.io
```

### 2. Describe your change as a feature

Before writing any code, use Spec Kit to specify your change:

```
speckit.specify <describe the change you want to make>
```

This creates a `spec.md` on a new feature branch with user stories,
requirements, and acceptance criteria.

### 3. Clarify and plan

```
speckit.clarify   # surface ambiguities in your spec
speckit.plan      # produce a technical design
speckit.tasks     # generate an ordered task list
```

### 4. Implement

```
speckit.implement  # work through tasks one by one
```

### 5. Open a Pull Request

Push your feature branch and open a PR against `main`.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the
   layer when doing a build.
2. Update the README.md with details of changes to the interface, this includes
   new environment variables, exposed ports, useful file locations and container
   parameters.
3. Increase the version numbers in any examples files and the README.md to the
   new version that this Pull Request would represent. The versioning scheme we
   use is [SemVer](http://semver.org/).
4. You may merge the Pull Request in once you have the sign-off of two other
   developers, or if you do not have permission to do that, you may request the
   second reviewer to merge it for you.
5. Keep PRs focused — ideally under ~300 lines of changes


## Branch Naming

Use descriptive, short names:

- `feature/short-description` — new feature
- `fix/short-description` — bug fix
- `chore/short-description` — maintenance
- `docs/short-description` — documentation
- `hotfix/short-description` — urgent fixes

### Examples

- `feature/add-json-validator`
- `fix/escape-file-paths-mac`

## Commit Messages

Follow Conventional Commits: `<type>(<scope>): <subject>`

### Types

- `feat` — new feature (triggers minor release)
- `fix` — bug fix (triggers patch release)
- `security` / `perf` — triggers patch release
- `docs` / `refactor` / `test` / `style` / `chore` / `ci` — no release

Keep subject lines <= 72 characters. Include a body when more context is needed.

### Examples

- `feat(probes): add community probe filtering`
- `fix(reports): correct scan count in summary`
- `docs: update contributing guide`
