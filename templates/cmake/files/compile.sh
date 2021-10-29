#!/usr/bin/env bash

cmake -Bbuild -H.
cmake --build build --target <NAME> -- -j4
