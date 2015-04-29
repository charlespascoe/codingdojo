import sys


class Dependencies:
    def __init__(self, packages):
        self.packages = packages

    def get_dependencies(self, package, deps=[]):
        if package not in self.packages: return []

        deps = list(deps)

        for dep in self.packages[package]:
            if dep not in deps:
                deps.append(dep)

                for new_dep in self.get_dependencies(dep, deps):
                    if new_dep not in deps:
                        deps.append(new_dep)

        deps.sort()
        return deps


if __name__ == '__main__':
    packages = {}

    with open('packages.txt') as f:
        for line in f.read().split('\n'):
            name, deps = line.split(' -> ')
            packages[name] = deps.split(' ')

    d = Dependencies(packages);

    for p in sys.argv[1:]:
        print('{} -> {}'.format(p, ' '.join(d.get_dependencies(p))))
