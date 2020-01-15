<template>
    <div class="calendar-container">
        <div id="calendar-nav">
            <div class="date-controller">
                <span class="date-control-btn" @click="subtractMonth">&lt;</span>
                <span id="current">{{ convertDate }}</span>
                <span class="date-control-btn" @click="addMonth">&gt;</span>
            </div>
            <div class="add-todo-btn" @click="showModal">
                추가하기
            </div>
        </div>
        <table id="calendar">
            <thead>
            <tr>
                <th>SUN</th>
                <th>MON</th>
                <th>TUE</th>
                <th>WED</th>
                <th>THR</th>
                <th>FRI</th>
                <th>SAT</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="weekIndex in 5" :key="weekIndex">
                <td class="date-cell" v-for="dateIndex in 7" :key="dateIndex">
                    <div class="day-number">
                        <div></div>
                    </div>
                    <TodoList :todoList="targetTodoList(weekIndex, dateIndex)"/>
                </td>
            </tr>
            </tbody>
        </table>
        <TodoModal v-show="isModalVisible" @close="closeModal" @addTodo="renderCalendar"/>
    </div>
</template>

<script>
    import TodoModal from "@/components/TodoModal";
    import todoService from "@/services/TodoService";
    import TodoList from "@/components/TodoList";

    export default {
        name: "Calendar",
        components: {TodoList, TodoModal},
        data: function () {
            return {
                isModalVisible: false,
                today: new Date(),
                currentDate: new Date(),
                currentYear: null,
                currentMonth: null,
                todoList: []
            }
        },
        computed: {
            convertDate: function () {
                return this.currentYear + "." + (this.currentMonth < 10 ? '0' + this.currentMonth : this.currentMonth);
            }
        },
        created: function () {
            this.setDate();
            this.loadTodo();
        },
        mounted: function () {
            this.renderCalendar();
        },
        methods: {
            loadTodo: async function () {
                this.todoList = await todoService.loadTodoList(this.currentYear, this.currentMonth)
            },
            targetTodoList: function (weekIndex, dateIndex) {
                let firstDate = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth(), 1);

                let targetDate = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth(), (weekIndex - 1) * 7 + dateIndex - firstDate.getDay());

                let targetTodoList = null;

                for (let key in this.todoList) {
                    let todo = this.todoList[key]
                    let split_date = todo.date.split('-');

                    if (targetDate - new Date(Number(split_date[0]), Number(split_date[1]) - 1, Number(split_date[2])) === 0) {
                        targetTodoList = [todo];
                        break;
                    }
                }

                return targetTodoList
            },
            renderCalendar: function () {
                let firstDate = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth(), 1);
                let firstDay = firstDate.getDay();
                let lastDate = new Date(this.currentDate.getFullYear(), this.currentDate.getMonth() + 1, 0);
                let last_datenum = lastDate.getDate();

                let count = 0;
                document.querySelectorAll(".calendar-container #calendar .date-cell").forEach((el) => {
                    let diff_days = count++ - firstDay;

                    let targetDate = this.addDays(firstDate, diff_days);

                    if (diff_days < 0) {
                        el.classList.add("diff-month");
                    } else if (diff_days > last_datenum - 1) {
                        el.classList.add("diff-month");
                    } else {
                        el.classList.remove("diff-month");
                    }

                    if (this.checkToday(targetDate)) {
                        el.classList.add("highlight-today");
                    } else if (el.classList.contains("highlight-today")) {
                        el.classList.remove("highlight-today")
                    }

                    el.querySelector('div').innerHTML = targetDate.getDate();
                });

                this.loadTodo();
            },
            subtractMonth: function () {
                this.currentDate.setMonth(this.currentDate.getMonth() - 1);
                this.setDate();
                this.renderCalendar();
            },
            addMonth: function () {
                this.currentDate.setMonth(this.currentDate.getMonth() + 1);
                this.setDate();
                this.renderCalendar();
            },
            setDate: function () {
                this.currentYear = this.currentDate.getFullYear();
                this.currentMonth = this.currentDate.getMonth() + 1;
            },
            addDays: function (date, days) {
                let result = new Date(date);
                result.setDate(result.getDate() + days);
                return result;
            },
            checkToday: function (targetDate) {
                return this.today.getFullYear() - targetDate.getFullYear() === 0 &&
                    this.today.getMonth() - targetDate.getMonth() === 0 &&
                    this.today.getDate() - targetDate.getDate() === 0;
            },
            showModal() {
                this.isModalVisible = true;
            },
            closeModal() {
                this.isModalVisible = false;
            }
        }
    }
</script>

<style scoped>
    .calendar-container {
        width: 100%;
        height: 100%;
    }

    .calendar-container #calendar-nav {
        position: relative;

        font-size: 24px;

        width: 100%;
        height: 5%;
    }

    .calendar-container #calendar-nav .date-controller {
        position: absolute;

        top: 50%;
        transform: translateY(-50%);

        width: 100%;
    }

    .calendar-container #calendar-nav .add-todo-btn {
        position: absolute;

        top: 50%;
        right: 20px;
        transform: translateY(-50%);

        background-color: #ff6813;
        color: white;

        font-size: 12px;
        font-weight: 700;
        width: 64px;
        height: 24px;
        line-height: 24px;

        border-radius: 4px;
    }

    .calendar-container #calendar-nav .date-control-btn {
        color: #999;
        font-weight: 400;
    }


    .calendar-container #current {
        color: #ff6813;
        font-weight: 700;

        margin-left: 10px;
        margin-right: 10px;
    }

    .calendar-container #calendar {
        table-layout: fixed;
        width: 100%;
        height: 95%;

        border-spacing: 0;
    }

    .calendar-container #calendar th {
        background: #bbb;
        color: white;
        border-bottom: 1px solid #f0f0f0;
    }

    .calendar-container #calendar th:nth-child(-n+6) {
        border-right: 1px solid #f0f0f0;
    }

    .calendar-container #calendar tr td {
        position: relative;

        overflow: hidden;
        word-wrap: break-word;

        min-height: 120px;
        height: 120px;

        border-top: 1px solid #f0f0f0;
        border-right: 1px solid #f0f0f0;

        vertical-align: top;

        box-sizing: border-box;
    }

    .calendar-container #calendar-nav tr td {
        background-color: yellow;
        color: white;
    }

    .calendar-container #calendar tr td:first-child {
        border-left: 1px solid #f0f0f0;
    }

    .calendar-container #calendar tr:last-child td {
        border-bottom: 1px solid #f0f0f0;
    }

    .calendar-container #calendar .date-cell .day-number {
        text-align: center;

        position: absolute;
        left: 0;
        top: 0;

        background: #fafafa;

        width: 100%;
        height: 20px;

        border-bottom: 1px solid #efefef;
    }

    .calendar-container #calendar .date-cell.highlight-today {
        border: 2px solid #ff6813;
    }

    .calendar-container #calendar .date-cell.diff-month {
        background-color: #fafafa;
    }

    .calendar-container #calendar .date-cell.highlight-today .day-number {
        color: #ff6813;
    }


</style>
