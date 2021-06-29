py_library(
    name = "cassandra-report-system-lib",
    srcs = [
        "cassandraReport.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-entity-manager",
        "//ecs/lib:ecs-system",
        "//simrunner/app/lib:api_lib",
    ],
)

py_library(
    name = "api-report-system-lib",
    srcs = [
        "apiReport.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-entity-manager",
        "//ecs/lib:ecs-system",
        "//simrunner/app/lib:api_lib",
    ],
)

py_library(
    name = "crit-system-lib",
    srcs = [
        "crit.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-system",
        "//mcSim/components:mcSim-dice-lib",
    ],
)

py_library(
    name = "report-system-lib",
    srcs = [
        "report.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-entity-manager",
        "//ecs/lib:ecs-system",
    ],
)

py_library(
    name = "roll-system-lib",
    srcs = [
        "roll.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-system",
        "//mcSim/components:mcSim-dice-lib",
    ],
)

py_library(
    name = "summarize-system-lib",
    srcs = [
        "summarize.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-system",
        "//mcSim/components:mcSim-general-components-lib",
    ],
)

py_library(
    name = "success-fail-system-lib",
    srcs = [
        "successFail.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-system",
        "//mcSim/components:mcSim-general-components-lib",
    ],
)

py_library(
    name = "success-fail-by-margin-system-lib",
    srcs = [
        "successFailByMargin.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-system",
        "//mcSim/components:mcSim-general-components-lib",
        "//mcSim/util:tuples-lib",
    ],
)

py_library(
    name = "roll-bonus-system-lib",
    srcs = [
        "rollBonus.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-system",
        "//mcSim/components:mcSim-roll-bonus-lib",
    ],
)

py_library(
    name = "threshold-reroll-system-lib",
    srcs = [
        "thresholdReroll.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-system",
        "//mcSim/components:mcSim-roll-bonus-lib",
        "//mcSim/util:tuples-lib",
    ],
)
