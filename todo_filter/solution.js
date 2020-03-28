function filterTodos(allTodoItems, selectedCategory) {
  return allTodoItems.filter(
    todoItem => todoItem.category === selectedCategory
  );
}

module.exports = filterTodos;
