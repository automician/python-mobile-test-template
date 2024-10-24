def relative_from_root(path: str):
    import python_mobile_test_template
    from pathlib import Path

    return (
        Path(python_mobile_test_template.__file__)
        .parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )
