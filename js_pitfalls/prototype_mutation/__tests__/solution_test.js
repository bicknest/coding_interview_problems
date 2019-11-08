test("it shows the solution to the problem", () => {
  const fooProto = {
    isBaz: function isBaz() {
      return this.state;
    },

    bar: function bar() {
      this.state = !this.state;
      return this;
    },

    meta: {
      name: "bim"
    },

    state: false
  };
  const foo1 = Object.create(fooProto);
  const foo2 = Object.create(fooProto);
  const foo3 = Object.create(fooProto);
  foo1.meta.name = "Bruce Lee";
  foo1.bar();
  foo2.meta.name = "Samuel L. Jackson";
  foo1.bar();
  foo2.bar();
  foo3.meta = { name: "Big Bird" };
  expect(foo1.meta.name).toEqual("Samuel L. Jackson");
  expect(foo1.isBaz()).toEqual(false);
  expect(foo2.isBaz()).toEqual(true);
  expect(foo2.meta.name).toEqual("Samuel L. Jackson");
  expect(foo3.meta.name).toEqual("Big Bird");
});
