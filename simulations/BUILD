py_library(
    name = "simulation-lib",
    srcs = [
        "simulation.py"
    ],
    visibility = ["//visibility:public"],
    deps = [
    ]
)

py_library(
    name = "firebolt-lib",
    srcs = [
        "firebolt.py"
    ],
    visibility = ["//visibility:public"],
    deps = [
        ":simulation-lib",
        "//ecs/lib:ecs-entity",
        "//ecs/lib:ecs-entity-manager",
        "//mcSim/components:mcSim-cover-lib",
        "//mcSim/components:mcSim-std-components-lib",
        "//mcSim/systems:crit-system-lib",
        "//mcSim/systems:report-system-lib",
        "//mcSim/systems:roll-bonus-system-lib",
        "//mcSim/systems:roll-system-lib",
        "//mcSim/systems:summarize-system-lib",
        "//mcSim/systems:success-fail-system-lib",
    ]
)

py_binary(
    name = "firebolt-sim",
    srcs = [
        "firebolt.py"
    ],
    main = "firebolt.py",
    deps = [
        ":firebolt-lib"
    ]
)