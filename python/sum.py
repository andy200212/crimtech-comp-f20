def sum(lst, n):
    for i in lst:
      k = n - i
      lst.remove(i)
      if k in lst:
        return True
      lst.append(i)
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()