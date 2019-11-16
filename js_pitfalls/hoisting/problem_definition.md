#Problem Definition

Replace the 'xxxxx' from below to make the tests all pass

test("test1", () => {
  var x = 1;
  expect(
    (function() {
      return x;
      var x = 2;
    })()
  ).toEqual(x);
});

test("test2", () => {
  function tester() {
    function number() {
      return 1;
    }

    (function() {
      expect(number()).toEqual(x);

      function number() {
        return 2;
      }
    })();
    expect(number()).toEqual(x);
  }
  tester();
});

test("test3", () => {
  function tester() {
    let i;
    function number() {
      return 1;
    }
    (function() {
      try {
        number();
      } catch {
        i = 1;
        expect(i).toEqual(x);
      }

      var number = function number() {
        return 2;
      };

      expect(number()).toEqual(x);
    })();

    expect(number()).toEqual(x);
  }
  tester();
});
