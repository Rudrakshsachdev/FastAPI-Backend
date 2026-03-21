const API = "http://127.0.0.1:8000/api/v1/todos";

async function fetchTodos() {
    const res = await fetch(API);
    const data = await res.json();

    const container = document.getElementById("todos");
    container.innerHTML = "";

    data.forEach(todo => {
        const div = document.createElement("div");
        div.className = "todo";

        div.innerHTML = `
            <span>${todo.title} (${todo.completed})</span>
            <div>
                <button onclick="toggleTodo(${todo.id}, ${todo.completed})">✔</button>
                <button onclick="deleteTodo(${todo.id})">❌</button>
            </div>
        `;

        container.appendChild(div);
    });
}


async function addTodo() {
    const titleInput = document.getElementById("title");
    const title = titleInput.value.trim();

    if (!title) {
        alert("Title cannot be empty");
        return;
    }

    await fetch(API, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            title: title,
            completed: false
        })
    });

    titleInput.value = "";
    fetchTodos();
}


async function deleteTodo(id) {
    await fetch(`${API}/${id}`, { method: "DELETE" });
    fetchTodos();
}


async function toggleTodo(id, completed) {
    const res = await fetch(`${API}/${id}`);
    const todo = await res.json();

    await fetch(`${API}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            title: todo.title,
            completed: !completed
        })
    });

    fetchTodos();
}


fetchTodos();