import VueRouter from 'vue-router';
import Calendar from "@/views/Calendar";

export const router = new VueRouter({
    mode: history,
    routes: [
        {
            path: '/',
            name: 'main',
            component: Calendar
        }
    ]
});
