import pytest
import subprocess
import testinfra
import pprint

# scope='session' uses the same container for all the tests;
# scope='function' uses a new container per test function.
@pytest.fixture(scope='session')
def host(request):
  # build local ./Dockerfile
  subprocess.check_call(['docker', 'build', '-t', 'web', '.'])
  # run a container
  docker_id = subprocess.check_output(
    ['docker', 'run', '-d', 'web']).decode().strip()
  # return a testinfra connection to the container
  yield testinfra.get_host("docker://" + docker_id)
  # at the end of the test suite, destroy the container
  subprocess.check_call(['docker', 'rm', '-f', docker_id])

@pytest.mark.parametrize('name,version', [
  ('python3', '3.6.4'),
])
def test_container_version(host, name, version):
  pkg = host.package(name)
  assert pkg.is_installed
  assert pkg.version.startswith(version)

@pytest.mark.parametrize('name,version', [
  ('Flask', '1.0.2'),
])
def test_pip_version(host, name, version):
  pkgs = host.pip_package.get_packages()
  pkg = pkgs[name]
  assert pkg
  assert pkg['version'] == version

def test_sshd_disabled(host):
  try:
    sshd = host.service('sshd')
    assert not sshd.is_running
    return
  except:
    return
  
  pytest.fail('sshd should not be running')