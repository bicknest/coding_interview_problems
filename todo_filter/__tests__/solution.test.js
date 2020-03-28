const filterTodos = require("../solution");
const _ = require("lodash");

test("tests that we properly filter out tasks", () => {
  const selectedCategory = "home";
  const allTodoItems = [
    { isDone: false, description: "vaccuum", category: "home" },
    { isDone: true, description: "dust", category: "home" },
    { isDone: false, escription: "email joe", category: "work" }
  ];
  // Make a deep copy of the array to test that the original array
  // was not mutated
  const todoItemsCopy = _.cloneDeep(allTodoItems);
  const filteredTodos = filterTodos(allTodoItems, selectedCategory);

  filteredTodos.forEach(todo => {
    expect(todo.category).toBe(selectedCategory);
  });
  expect(filteredTodos).toEqual([
    { isDone: false, description: "vaccuum", category: "home" },
    { isDone: true, description: "dust", category: "home" }
  ]);

  // Ensure we don't mutate original array
  expect(allTodoItems).toEqual(todoItemsCopy);

  expect(filterTodos([])).toEqual([]);
});
