py_library(
    name = "report-system-lib",
    srcs = [
        "report.py"
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-system"
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