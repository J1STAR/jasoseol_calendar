import axios from 'axios'

export default {
    async addTodo(year, month, date, event) {
        let url = `/api/todo/${year}/${month}/${date}/`;
        let data = {"event": event};

        let getResultAddTodo = async () => {
            let response = await axios.post(url, data);
            return response.data
        };

        return await getResultAddTodo();
    },
    async loadTodoList(year, month) {
        let url = `/api/todo/${year}/${month}/`;

        let getTodoList = async () => {
            let response = await axios.get(url);
            return response.data
        };

        return await getTodoList();
    }
}
