import subprocess
import sys
import xml.etree.ElementTree as ET

CONFIG_PATH = r".\CurrentConfig.config"


def load_packages(config_path):
    tree = ET.parse(config_path)
    root = tree.getroot()
    return [(pkg.get("id"), pkg.get("version")) for pkg in root.findall("package")]


def install_package(pkg_id, version):
    spec = f"{pkg_id}={version}"
    cmd = ["cmd", "/c", "tcpkg", "install", spec, "-y", "--allow-downgrade", "--all-sources"]
    print(f"\n=== Installing {spec} ===")
    result = subprocess.run(cmd)
    return result.returncode == 0


def main():
    config_path = sys.argv[1] if len(sys.argv) > 1 else CONFIG_PATH
    packages = load_packages(config_path)
    print(f"Found {len(packages)} packages in {config_path}")

    failed = []
    for pkg_id, version in packages:
        ok = install_package(pkg_id, version)
        if not ok:
            failed.append(f"{pkg_id}={version}")

    print("\n\n=== Summary ===")
    print(f"Installed: {len(packages) - len(failed)}/{len(packages)}")
    if failed:
        print("Failed packages:")
        for spec in failed:
            print(f"  - {spec}")
    else:
        print("All packages installed successfully.")


if __name__ == "__main__":
    main()
