def abs_path_from_project(relative_path: str):
    import python_mobile_test_template
    from pathlib import Path

    return (
        Path(python_mobile_test_template.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
