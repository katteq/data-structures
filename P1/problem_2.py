import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    res = []

    if path == None or suffix == None:
        return res

    if os.path.isfile(path):
        if path.endswith(suffix):
            res.append(path)
        else:
            return res
    elif os.path.isdir(path):
        current_dir_items = os.listdir(path)
        for item in current_dir_items:
            name = os.path.join(path, item)
            if os.path.isfile(name):
                if name.endswith(suffix):
                    res.append(name)
                else:
                    continue
            elif os.path.isdir(path):
                res.extend(find_files(suffix, name))

    return res

def test(suffix, input_dir, expected_output):
    """
    Test funstion.

    Args:
      suffix(str): file suffix
      input_dir(str): the directory where to search
      expected_output(list): expected output

    Returns: void
    """
    res = find_files(suffix, input_dir)
    print("Pass" if res == expected_output else "Fail")


test(".c", "./testdir/", ['./testdir/subdir3/subsubdir1/b.c',
                          './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c'])

test(".gitkeep", "./testdir/",
     ['./testdir/subdir4/.gitkeep', './testdir/subdir2/.gitkeep'])
test(".bda", "./testdir/", [])
test(None, "./testdir/", [])
test(None, None, [])
test(".c", None, [])
