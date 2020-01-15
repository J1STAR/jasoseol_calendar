<template>
    <div id="todo-list-container">
        <div class="todo-list">
            <div class="todo" v-for="todo in todoList" :key="todo.id" @click="alertTodo()">
                {{ todo.event }}
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "TodoList",
        props: {
            todoList: {type: Array}
        },
        methods: {
            alertTodo: function() {
                alert(`${this.todoList[0].date}의 할 일은 ${this.todoList[0].event}입니다.`)
            }
        }
    }
</script>

<style scoped>
    #todo-list-container {
        padding-top: 30px;

        height: calc(100% - 20px);
    }

    #todo-list-container .todo-list {
        text-align: left;
    }

    #todo-list-container .todo-list .todo {
        padding-left: 20px;
        width: 100%;
    }
</style>
