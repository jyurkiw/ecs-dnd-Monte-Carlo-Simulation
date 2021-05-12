py_library(
    name = "crit-system-lib",
    srcs = [
        "crit.py"
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-system",
        "//mcSim/components:mcSim-dice-lib"
    ]
)

py_library(
    name = "report-system-lib",
    srcs = [
        "report.py"
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-system",
        "//ecs/lib:ecs-entity-manager"
    ]
)

py_library(
    name = "roll-system-lib",
    srcs = [
        "roll.py"
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-system",
        "//mcSim/components:mcSim-dice-lib"
    ]
)

py_library(
    name="summarize-system-lib",
    srcs=[
        "summarize.py"
    ],
    visibility = ["//visibility:public"],
    deps=[
        "//ecs/lib:ecs-system",
        "//mcSim/components:mcSim-general-components-lib"
    ]
)

py_library(
    name="success-fail-system-lib",
    srcs=[
        "successFail.py"
    ],
    visibility = ["//visibility:public"],
    deps=[
        "//ecs/lib:ecs-system",
        "//mcSim/components:mcSim-general-components-lib"
    ]
)

py_library(
    name="roll-bonus-system-lib",
    srcs=[
        "rollBonus.py"
    ],
    visibility = ["//visibility:public"],
    deps=[
        "//ecs/lib:ecs-system",
        "//mcSim/components:mcSim-roll-bonus-lib",
    ]
)