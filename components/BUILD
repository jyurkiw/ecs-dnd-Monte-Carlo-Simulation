py_library(
    name = "mcSim-cover-lib",
    srcs = [
        "cover.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-component",
    ],
)

py_library(
    name = "mcSim-dice-lib",
    srcs = [
        "dice.py"
    ],
    visibility = ["//visibility:public"],
    deps=[
        "//ecs/components:ecs-value-component-lib",
        "//ecs/lib:ecs-component"
    ]
)

py_library(
    name = "mcSim-general-components-lib",
    srcs = [
        "general.py"
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-component",
        "//ecs/components:ecs-value-component-lib"
    ]
)

py_library(
    name = "mcSim-roll-bonus-lib",
    srcs = [
        "rollBonus.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/components:ecs-value-component-lib",
    ],
)

py_library(
    name = "mcSim-target-number-lib",
    srcs = [
        "targetNumber.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/components:ecs-value-component-lib",
    ],
)

py_library(
    name = "mcSim-std-components-lib",
    srcs = [
        "dice.py",
        "rollBonus.py",
        "targetNumber.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//mcSim/components:mcSim-dice-lib",
        "//mcSim/components:mcSim-roll-bonus-lib",
        "//mcSim/components:mcSim-target-number-lib",
    ],
)