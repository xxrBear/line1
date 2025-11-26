import { Outlet, Link } from "react-router-dom";

const AdminLayout = () => {
    return (
        <>
            <aside>
                <ul >
                    <li><Link to="/" >仪表盘</Link></li>
                    <li><Link to="/articles">文章管理</Link></li>
                </ul>
            </aside>

            <main>
                <Outlet />
            </main>
        </>
    );
};

export default AdminLayout;
