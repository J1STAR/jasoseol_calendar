<template>
    <div id="todo-modal-container">
        <div class="modal-shadow">
            <div class="modal">
                <header class="modal-header">
                    <slot name="header">
                        Todo

                        <button
                                type="button"
                                class="btn-close"
                                @click="closeModal"
                        >
                            x
                        </button>
                    </slot>
                </header>
                <section class="modal-body">
                    <slot name="body">
                        <form class="todo-form">
                            <table>
                                <tr>
                                    <th>Date</th>
                                    <td><input type="date" class="date" name="date"></td>
                                </tr>
                                <tr>
                                    <th>Event</th>
                                    <td><input type="text" class="event" name="event"></td>
                                </tr>
                            </table>
                        </form>
                    </slot>
                </section>
                <footer class="modal-footer">
                    <slot name="footer">
                        <button
                                type="button"
                                class="btn-orange"
                                @click="addTodo"
                        >
                            Add Todo
                        </button>
                    </slot>
                </footer>
            </div>
        </div>
    </div>
</template>

<script>
    import todoService from "@/services/TodoService"

    export default {
        name: "TodoModal",
        methods: {

            closeModal() {
                this.$emit('close');
                this.resetField();
            },
            addTodo() {
                let date_field = document.querySelector('.todo-form').date;
                let event_field = document.querySelector('.todo-form').event;

                let split_date_field = date_field.value.split('-');
                let year = split_date_field[0];
                let month = split_date_field[1];
                let date = split_date_field[2];

                let event_value = event_field.value;
                todoService.addTodo(year, month, date, event_value);

                this.closeModal();

                this.$emit('addTodo');
            },
            resetField() {
                let date_field = document.querySelector('.todo-form').date;
                let event_field = document.querySelector('.todo-form').event;

                date_field.value = "";
                event_field.value = "";
            }
        }
    }
</script>

<style scoped>
    #todo-modal-container .modal-shadow {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: rgba(0, 0, 0, 0.3);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    #todo-modal-container .modal-shadow .modal {
        background: #FFFFFF;
        box-shadow: 2px 2px 20px 1px;

        width: 500px;

        overflow-x: auto;
        display: flex;
        flex-direction: column;
    }

    #todo-modal-container .modal-shadow .modal .modal-header,
    .modal-footer {
        padding: 15px;
        display: flex;
    }

    #todo-modal-container .modal-shadow .modal .modal-header {
        border-bottom: 1px solid #eeeeee;
        color: #ff6813;
        justify-content: space-between;
    }

    #todo-modal-container .modal-shadow .modal .modal-footer {
        border-top: 1px solid #eeeeee;
        justify-content: flex-end;
    }

    #todo-modal-container .modal-shadow .modal .modal-body {
        position: relative;
        padding: 20px 10px;
    }

    #todo-modal-container .modal-shadow .modal .modal-body .todo-form {
        text-align: left;

        font-size: 24px;
    }

    #todo-modal-container .modal-shadow .modal .modal-body .todo-form td {
        width: 100%;
    }

    #todo-modal-container .modal-shadow .modal .modal-body .todo-form td input {
        width: 100%;

        border: none;
        border-bottom: 2px solid #ff6813;
    }

    #todo-modal-container .modal-shadow .modal .modal-body .todo-form th, td input {
        text-align: left;


        font-size: 24px;
    }

    #todo-modal-container .modal-shadow .modal .btn-close {
        border: none;
        font-size: 20px;
        cursor: pointer;
        font-weight: bold;
        color: #ff6813;
        background: transparent;
    }

    #todo-modal-container .modal-shadow .modal .btn-orange {
        color: white;
        background: #ff6813;
        border: 1px solid #ff6813;
        border-radius: 2px;
    }
</style>
