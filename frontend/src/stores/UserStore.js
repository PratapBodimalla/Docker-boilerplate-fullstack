import { makeAutoObservable } from "mobx";
import axios from "axios";

class UserStore {
    users = [];

    constructor() {
        makeAutoObservable(this);
    }

    async fetchUsers() {
        try {
            const response = await axios.get("http://localhost:5000/users");
            this.users = response.data;
        } catch (error) {
            console.error("Failed to fetch users:", error);
        }
    }
}

const userStore = new UserStore();
export default userStore;
