py_library(
    name="report-test-lib",
    srcs=[
        "report_test.py"
    ],
    deps=[
        "//ecs/lib:ecs-entity",
        "//mcSim/components:mcSim-general-components-lib",
        "//mcSim/systems:report-system-lib"
    ],
    visibility = ["//visibility:public"],
)

py_test(
    name="report-test",
    size="small",
    srcs=[
        "report_test.py"
    ],
    main="report_test.py",
    deps=[
        ":report-test-lib",
    ]
)

py_library(
    name="roll-test-lib",
    srcs=[
        "roll_test.py",
    ],
    deps=[
        "//ecs/lib:ecs-entity",
        "//mcSim/systems:roll-system-lib",
        "//mcSim/components:mcSim-dice-lib"
    ],
    visibility = ["//visibility:public"],
)

py_test(
    name="roll-test",
    size="small",
    srcs=[
        "roll_test.py"
    ],
    main="roll_test.py",
    deps=[
        ":roll-test-lib",
    ]
)