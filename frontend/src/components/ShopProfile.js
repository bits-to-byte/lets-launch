import React,{ useEffect} from "react";

import {Link} from 'react-router-dom';

import { makeStyles } from "@material-ui/core/styles";
import {Grid, Typography, Box, Hidden} from "@material-ui/core";
import Paper from '@material-ui/core/Paper';
import ButtonBase from '@material-ui/core/ButtonBase';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAddressBook,faPhone,faMailBulk } from '@fortawesome/free-solid-svg-icons'
import FacebookIcon from '@material-ui/icons/Facebook';
import InstagramIcon from '@material-ui/icons/Instagram';
import 'font-awesome/css/font-awesome.min.css';

import {
    shopDetail,
    bag,
    loading,
    errorMessage,
    infoMessage,
    placeOrderFormDialogOpen,
} from "../selectors/customerSelectors";

import {
    getProfileShop, hideErrorInfo,
    placeOrder,
    togglePlaceOrderFormDialog,
    updateBagProductCount
} from "../actions/customerActions";

import {connect} from "react-redux";
import {useParams, useRouteMatch} from "react-router-dom";

const useStyles = makeStyles({
    root: {
        maxWidth: 345,
    },
});

function ProfileView({
                           //state
                           shopDetail,
                         getProfileShop,
                     }){
    const { shopId } = useParams();
    const match = useRouteMatch();

    // console.log(shopId);
    useEffect(() => {
        getProfileShop(shopId);
    }, []);
    const classes = useStyles();

    const path = `${match.path}`.replace(":shopId", shopId);

    let shopProductsData = shopDetail["shop_products"] || [];
    console.log(shopDetail)
    return(

        <Box
            display="flex"
            justifyContent="center"
            alignItems="center"
            minHeight="90vh"
        >
            <Card className={classes.root}>

                <CardActionArea>
                    <h2 style={{marginLeft:'115px'}}>Shop Card</h2>

                    <CardMedia
                        component="img"
                        alt="Contemplative Reptile"
                        height="200"
                        image="https://upload.wikimedia.org/wikipedia/commons/8/8e/Shop.svg"
                        title="Contemplative Reptile"
                    />
                    <CardContent>
                        <Typography gutterBottom variant="h5" component="h2">
                            <FontAwesomeIcon icon={faMailBulk} /> Email: {shopDetail.email}
                        </Typography>
                        <Typography gutterBottom variant="h5" component="h2">
                            <FontAwesomeIcon icon={faPhone} /> Phone: {shopDetail.phone}
                        </Typography>
                        <Typography gutterBottom variant="h5" component="h2">
                            <FontAwesomeIcon icon={faAddressBook} /> Address: {shopDetail.address}
                        </Typography>

                        <Typography variant="body2" color="textSecondary" component="p">
                            <FacebookIcon/> Facebook: {shopDetail.fbUrl}
                        </Typography>
                        <Typography variant="body2" color="textSecondary" component="p">
                            <InstagramIcon/> Instagram: {shopDetail.instaUrl}
                        </Typography>
                    </CardContent>
                </CardActionArea>
                <CardActions>
                    <Button size="small" color="primary">
                        <Link to={shopDetail.discordUrl}>Join Discord</Link>
                    </Button>
                    <Button size="small" color="primary">
                        <Link to={'../'+'s/'+shopDetail.id}>Go to Shop</Link>
                    </Button>
                </CardActions>
            </Card>

        </Box>
    )
}

const mapStateToProps = (state) => {
    return {
        loading: loading(state),
        shopDetail: shopDetail(state),
        bag: bag(state),
        placeOrderFormDialogOpen: placeOrderFormDialogOpen(state),
        error: errorMessage(state),
        info: infoMessage(state),
    };
};

const mapDispatchToProps = (dispatch) => {
    return {
        getProfileShop: (shopId) => dispatch(getProfileShop(shopId)),
        updateProductCount: (bag, product, count) =>
            dispatch(updateBagProductCount(bag, product, count)),
        togglePlaceOrderFormDialog: () => dispatch(togglePlaceOrderFormDialog),
        placeOrder: (shopDetail, orderData) =>
            dispatch(placeOrder(shopDetail, orderData)),
        hideErrorInfo: () => dispatch(hideErrorInfo()),
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(ProfileView);