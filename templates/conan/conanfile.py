from conans import ConanFile, CMake

class <NAME>Conan(ConanFile):
    name = "<NAME>"
    version = "0.0.1"
    license = "MIT"

    generators = "cmake", "cmake_paths", "cmake_find_package", "virtualbuildenv"

    requires = (
        "fmt/8.0.1",
        "gtest/cci.20210126",
        "benchmark/1.6.0"
    )

    def imports(self):
        self.copy('*.so*', dst='lib', src='lib')

    def configure(self):
        self.options["fmt"].shared = False

    def build(self):
        cmake = CMake(self, generator='Ninja')
        cmake.configure()
        cmake.build()
