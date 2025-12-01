import {
    Box,
    Grid,
    LinearProgress,
    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Typography,
} from '@mui/material';

const articleData = [
    { id: 1, title: '如何学习 React', author: 'Alice', views: 120, status: '已发布' },
    { id: 2, title: 'Node.js 入门', author: 'Bob', views: 80, status: '草稿' },
    { id: 3, title: 'JavaScript 深拷贝技巧', author: 'Charlie', views: 150, status: '已发布' },
];

const Dashboard = () => {
    return (
        <Box sx={{ padding: 3 }}>
            {/* 统计卡片 */}
            <Grid container spacing={3}>
                <Grid item xs={12} sm={6} md={3}>
                    <Paper sx={{ padding: 2 }}>
                        <Typography variant="subtitle1">总文章数</Typography>
                        <Typography variant="h5">120</Typography>
                    </Paper>
                </Grid>
                <Grid item xs={12} sm={6} md={3}>
                    <Paper sx={{ padding: 2 }}>
                        <Typography variant="subtitle1">今日访问量</Typography>
                        <Typography variant="h5">450</Typography>
                    </Paper>
                </Grid>
                <Grid item xs={12} sm={6} md={3}>
                    <Paper sx={{ padding: 2 }}>
                        <Typography variant="subtitle1">评论数</Typography>
                        <Typography variant="h5">85</Typography>
                    </Paper>
                </Grid>
                <Grid item xs={12} sm={6} md={3}>
                    <Paper sx={{ padding: 2 }}>
                        <Typography variant="subtitle1">作者人数</Typography>
                        <Typography variant="h5">12</Typography>
                    </Paper>
                </Grid>
            </Grid>

            {/* 文章发布进度 */}
            <Paper sx={{ padding: 2, marginTop: 3 }}>
                <Typography variant="subtitle1" gutterBottom>
                    文章发布进度
                </Typography>
                <LinearProgress variant="determinate" value={75} />
            </Paper>

            {/* 最新文章表格 */}
            <Paper sx={{ padding: 2, marginTop: 3 }}>
                <Typography variant="subtitle1" gutterBottom>
                    最新文章
                </Typography>
                <TableContainer>
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell>文章标题</TableCell>
                                <TableCell>作者</TableCell>
                                <TableCell>浏览量</TableCell>
                                <TableCell>状态</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {articleData.map((row) => (
                                <TableRow key={row.id}>
                                    <TableCell>{row.title}</TableCell>
                                    <TableCell>{row.author}</TableCell>
                                    <TableCell>{row.views}</TableCell>
                                    <TableCell>{row.status}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </Paper>

            {/* 访问趋势 */}
            <Paper sx={{ padding: 2, marginTop: 3 }}>
                <Typography variant="subtitle1" gutterBottom>
                    访问趋势
                </Typography>
                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
                    <Box>
                        <Typography variant="body2">11月1日: 200 次</Typography>
                        <LinearProgress variant="determinate" value={40} />
                    </Box>
                    <Box>
                        <Typography variant="body2">11月2日: 450 次</Typography>
                        <LinearProgress variant="determinate" value={90} />
                    </Box>
                    <Box>
                        <Typography variant="body2">11月3日: 300 次</Typography>
                        <LinearProgress variant="determinate" value={60} />
                    </Box>
                </Box>
            </Paper>
        </Box>
    );
};

export default Dashboard;
