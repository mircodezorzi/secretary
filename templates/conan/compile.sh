#!/usr/bin/env bash

cd build
conan install .
conan build .
