py_library(
    name = "report-test-lib",
    srcs = [
        "report_test.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-entity",
        "//mcSim/components:mcSim-general-components-lib",
        "//mcSim/systems:report-system-lib",
    ],
)

py_test(
    name = "report-test",
    size = "small",
    srcs = [
        "report_test.py",
    ],
    main = "report_test.py",
    deps = [
        ":report-test-lib",
    ],
)

py_library(
    name = "roll-test-lib",
    srcs = [
        "roll_test.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-entity",
        "//mcSim/components:mcSim-dice-lib",
        "//mcSim/systems:roll-system-lib",
    ],
)

py_test(
    name = "roll-test",
    size = "small",
    srcs = [
        "roll_test.py",
    ],
    main = "roll_test.py",
    deps = [
        ":roll-test-lib",
    ],
)

py_library(
    name = "successFail-test-lib",
    srcs = [
        "successFail_test.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//ecs/lib:ecs-entity",
        "//ecs/lib:ecs-entity-manager",
        "//mcSim/components:mcSim-dice-lib",
        "//mcSim/components:mcSim-roll-bonus-lib",
        "//mcSim/components:mcSim-target-number-lib",
        "//mcSim/systems:success-fail-system-lib",
    ],
)

py_test(
    name = "successFail-test",
    size = "small",
    srcs = [
        "successFail_test.py",
    ],
    main = "successFail_test.py",
    deps = [
        ":successFail-test-lib",
    ],
)
