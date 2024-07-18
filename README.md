### Default commits

Commits should be added by Issues, with the default:

`<type>(scope): <description> <ref-id>`

### Default branches

Branches should be added by Issues, always created by __"dev"__, with the default:

`feature/<branch-name>`

### Run
```sh
git clone https://github.com/fabricadesoftware-ifc/fabricaHistologia_backend.git
```
```sh
cd fabricaHistologia_backend
```
```sh
pdm install
```
```sh
pdm migrate
```
```sh
pdm run dev
```
