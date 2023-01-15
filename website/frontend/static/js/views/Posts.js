import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor() {
        super();
        this.setTitle("Posts");
    }

    async getHtml() {
        return `
            <h1> Recent Posts</h1>
            <p>
                So maybe here goes some posts, comments on runs etc...
            </p>
            <p>
                <a href="/" data-link>Back to Dashboard...</a>.
            </p>
        `;        
    }
}