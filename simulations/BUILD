py_library(
    name = "simulation-lib",
    srcs = [
        "simulation.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
    ],
)

py_library(
    name = "crystal-hammer-lib",
    srcs = [
        "crystalhammer.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        ":simulation-lib",
        "//ecs/lib:ecs-entity",
        "//ecs/lib:ecs-entity-manager",
        "//mcSim/components:mcSim-cover-lib",
        "//mcSim/components:mcSim-std-components-lib",
        "//mcSim/data:stat-data-lib",
        "//mcSim/systems:api-report-system-lib",
        "//mcSim/systems:crit-system-lib",
        "//mcSim/systems:roll-bonus-system-lib",
        "//mcSim/systems:roll-system-lib",
        "//mcSim/systems:success-fail-system-lib",
        "//mcSim/systems:summarize-system-lib",
        "//mcSim/util:report-writer-lib",
    ],
)

py_binary(
    name = "crystal-hammer-sim",
    srcs = [
        "crystalhammer.py",
    ],
    main = "crystalhammer.py",
    deps = [
        ":crystal-hammer-lib",
    ],
)

py_library(
    name = "firebolt-lib",
    srcs = [
        "firebolt.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        ":simulation-lib",
        "//ecs/lib:ecs-entity",
        "//ecs/lib:ecs-entity-manager",
        "//mcSim/components:mcSim-cover-lib",
        "//mcSim/components:mcSim-std-components-lib",
        "//mcSim/data:stat-data-lib",
        "//mcSim/systems:api-report-system-lib",
        "//mcSim/systems:crit-system-lib",
        "//mcSim/systems:roll-bonus-system-lib",
        "//mcSim/systems:roll-system-lib",
        "//mcSim/systems:success-fail-system-lib",
        "//mcSim/systems:summarize-system-lib",
        "//mcSim/util:report-writer-lib",
    ],
)

py_binary(
    name = "firebolt-sim",
    srcs = [
        "firebolt.py",
    ],
    main = "firebolt.py",
    deps = [
        ":firebolt-lib",
    ],
)

py_library(
    name = "frostbite-lib",
    srcs = [
        "frostbite.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        ":simulation-lib",
        "//ecs/lib:ecs-entity",
        "//ecs/lib:ecs-entity-manager",
        "//mcSim/components:mcSim-cover-lib",
        "//mcSim/components:mcSim-std-components-lib",
        "//mcSim/data:stat-data-lib",
        "//mcSim/systems:api-report-system-lib",
        "//mcSim/systems:crit-system-lib",
        "//mcSim/systems:roll-bonus-system-lib",
        "//mcSim/systems:roll-system-lib",
        "//mcSim/systems:success-fail-system-lib",
        "//mcSim/systems:summarize-system-lib",
        "//mcSim/util:report-writer-lib",
    ],
)

py_binary(
    name = "frostbite-sim",
    srcs = [
        "frostbite.py",
    ],
    main = "frostbite.py",
    deps = [
        ":frostbite-lib",
    ],
)

py_library(
    name = "magnetic-sling-lib",
    srcs = [
        "magneticSling.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        ":simulation-lib",
        "//ecs/lib:ecs-entity",
        "//ecs/lib:ecs-entity-manager",
        "//mcSim/components:mcSim-cover-lib",
        "//mcSim/components:mcSim-std-components-lib",
        "//mcSim/data:stat-data-lib",
        "//mcSim/systems:api-report-system-lib",
        "//mcSim/systems:crit-system-lib",
        "//mcSim/systems:roll-bonus-system-lib",
        "//mcSim/systems:roll-system-lib",
        "//mcSim/systems:success-fail-system-lib",
        "//mcSim/systems:summarize-system-lib",
        "//mcSim/systems:threshold-reroll-system-lib",
        "//mcSim/util:report-writer-lib",
    ],
)

py_binary(
    name = "magnetic-sling-sim",
    srcs = [
        "magneticSling.py",
    ],
    main = "magneticSling.py",
    deps = [
        ":magnetic-sling-lib",
    ],
)

py_library(
    name = "radiantflash-lib",
    srcs = [
        "radiantflash.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        ":simulation-lib",
        "//ecs/lib:ecs-entity",
        "//ecs/lib:ecs-entity-manager",
        "//mcSim/components:mcSim-cover-lib",
        "//mcSim/components:mcSim-std-components-lib",
        "//mcSim/data:stat-data-lib",
        "//mcSim/systems:api-report-system-lib",
        "//mcSim/systems:crit-system-lib",
        "//mcSim/systems:roll-bonus-system-lib",
        "//mcSim/systems:roll-system-lib",
        "//mcSim/systems:success-fail-by-margin-system-lib",
        "//mcSim/systems:success-fail-system-lib",
        "//mcSim/systems:summarize-system-lib",
        "//mcSim/util:report-writer-lib",
    ],
)

py_binary(
    name = "radiantflash-sim",
    srcs = [
        "radiantflash.py",
    ],
    main = "radiantflash.py",
    deps = [
        ":radiantflash-lib",
    ],
)
