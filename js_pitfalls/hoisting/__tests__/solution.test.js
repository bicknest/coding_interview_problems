test("variable hoisting basics", () => {
  var x = 1;
  expect(
    (function() {
      return x;
      var x = 2;
    })()
  ).toEqual(undefined);
});

test("function declaration hoisting", () => {
  function tester() {
    function number() {
      return 1;
    }

    (function() {
      expect(number()).toEqual(2);

      function number() {
        return 2;
      }
    })();
    expect(number()).toEqual(1);
  }
  tester();
});

test("function expression hoisting", () => {
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
        expect(i).toEqual(1);
      }

      var number = function number() {
        return 2;
      };

      expect(number()).toEqual(2);
    })();

    expect(number()).toEqual(1);
  }
  tester();
});
