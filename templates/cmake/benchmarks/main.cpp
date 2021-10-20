#include <benchmark/benchmark.h>

#include <fmt/format.h>

static void HelloWorld(benchmark::State& state) {
  for (auto _ : state) {
    fmt::print("Hello, World!");
  }
}
BENCHMARK(HelloWorld);

BENCHMARK_MAIN();
