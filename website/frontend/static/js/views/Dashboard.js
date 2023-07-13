import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor() {
        super();
        this.setTitle("Dashboard");
    }

    async getHtml() {
        return `
<<<<<<< HEAD
            <h1>Nug Run Club 2023!</h1>
=======
            <h2>Nug Run Club 2023!</h2>
>>>>>>> c46b4567611d73d7a2b6937b843387af7dd77092
            <p>
                Watch this space! Here we'll put the current month pie with some graphs of current progress.       
            </p>
            <img src="images/NRCLogo.jpeg" alt="NRC Logo" style="max-width: 100%; height: auto; ">
            <img src="images/pie.png" alt="Current Pie" style="max-width: 100%; height: auto;">
            <p>
                <a href="/lastMonth" data-link>View previous month winners...</a>.
            </p>
        `;
    }
}