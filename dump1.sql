--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Drop databases (except postgres and template1)
--

DROP DATABASE docker;




--
-- Drop roles
--

DROP ROLE saidamir;


--
-- Roles
--

CREATE ROLE saidamir;
ALTER ROLE saidamir WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:d9J1+VNpA/5RmYIDJ3tWjQ==$wTIRE8Z8uliL/NmKqbrNDt1bjoUFyXFVuXc7I9Hmxo4=:I84k9iJ9wsDtl3wWoMD1Boj76a12DBKC55NW7EJVDoA=';






--
-- Databases
--

--
-- Database "template1" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg110+1)
-- Dumped by pg_dump version 14.1 (Debian 14.1-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

UPDATE pg_catalog.pg_database SET datistemplate = false WHERE datname = 'template1';
DROP DATABASE template1;
--
-- Name: template1; Type: DATABASE; Schema: -; Owner: saidamir
--

CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE template1 OWNER TO saidamir;

\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: COMMENT; Schema: -; Owner: saidamir
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: template1; Type: DATABASE PROPERTIES; Schema: -; Owner: saidamir
--

ALTER DATABASE template1 IS_TEMPLATE = true;


\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: ACL; Schema: -; Owner: saidamir
--

REVOKE CONNECT,TEMPORARY ON DATABASE template1 FROM PUBLIC;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


--
-- PostgreSQL database dump complete
--

--
-- Database "docker" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg110+1)
-- Dumped by pg_dump version 14.1 (Debian 14.1-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: docker; Type: DATABASE; Schema: -; Owner: saidamir
--

CREATE DATABASE docker WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE docker OWNER TO saidamir;

\connect docker

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO saidamir;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO saidamir;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO saidamir;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO saidamir;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO saidamir;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO saidamir;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: core_basket; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_basket (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.core_basket OWNER TO saidamir;

--
-- Name: core_basket_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_basket_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_basket_id_seq OWNER TO saidamir;

--
-- Name: core_basket_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_basket_id_seq OWNED BY public.core_basket.id;


--
-- Name: core_basket_products; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_basket_products (
    id bigint NOT NULL,
    basket_id bigint NOT NULL,
    productorder_id bigint NOT NULL
);


ALTER TABLE public.core_basket_products OWNER TO saidamir;

--
-- Name: core_basket_products_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_basket_products_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_basket_products_id_seq OWNER TO saidamir;

--
-- Name: core_basket_products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_basket_products_id_seq OWNED BY public.core_basket_products.id;


--
-- Name: core_brand; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_brand (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    title character varying(255) NOT NULL,
    logo character varying(100) NOT NULL,
    is_active boolean NOT NULL
);


ALTER TABLE public.core_brand OWNER TO saidamir;

--
-- Name: core_brand_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_brand_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_brand_id_seq OWNER TO saidamir;

--
-- Name: core_brand_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_brand_id_seq OWNED BY public.core_brand.id;


--
-- Name: core_catalog; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_catalog (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    title character varying(255) NOT NULL,
    is_active boolean NOT NULL,
    lft integer NOT NULL,
    rght integer NOT NULL,
    tree_id integer NOT NULL,
    level integer NOT NULL,
    parent_id bigint,
    title_ru character varying(255),
    title_uz character varying(255),
    title_en character varying(255),
    image character varying(100),
    CONSTRAINT core_catalog_level_check CHECK ((level >= 0)),
    CONSTRAINT core_catalog_lft_check CHECK ((lft >= 0)),
    CONSTRAINT core_catalog_rght_check CHECK ((rght >= 0)),
    CONSTRAINT core_catalog_tree_id_check CHECK ((tree_id >= 0))
);


ALTER TABLE public.core_catalog OWNER TO saidamir;

--
-- Name: core_catalog_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_catalog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_catalog_id_seq OWNER TO saidamir;

--
-- Name: core_catalog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_catalog_id_seq OWNED BY public.core_catalog.id;


--
-- Name: core_comment; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_comment (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    text text NOT NULL,
    is_active boolean NOT NULL,
    lft integer NOT NULL,
    rght integer NOT NULL,
    tree_id integer NOT NULL,
    level integer NOT NULL,
    parent_id bigint,
    product_id bigint NOT NULL,
    user_id bigint NOT NULL,
    CONSTRAINT core_comment_level_check CHECK ((level >= 0)),
    CONSTRAINT core_comment_lft_check CHECK ((lft >= 0)),
    CONSTRAINT core_comment_rght_check CHECK ((rght >= 0)),
    CONSTRAINT core_comment_tree_id_check CHECK ((tree_id >= 0))
);


ALTER TABLE public.core_comment OWNER TO saidamir;

--
-- Name: core_comment_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_comment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_comment_id_seq OWNER TO saidamir;

--
-- Name: core_comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_comment_id_seq OWNED BY public.core_comment.id;


--
-- Name: core_delivery; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_delivery (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    delivery_price integer NOT NULL,
    region_id bigint,
    CONSTRAINT core_delivery_delivery_price_check CHECK ((delivery_price >= 0))
);


ALTER TABLE public.core_delivery OWNER TO saidamir;

--
-- Name: core_delivery_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_delivery_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_delivery_id_seq OWNER TO saidamir;

--
-- Name: core_delivery_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_delivery_id_seq OWNED BY public.core_delivery.id;


--
-- Name: core_order; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_order (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    payment_type character varying(255) NOT NULL,
    order_status character varying(255) NOT NULL,
    payment_status character varying(255) NOT NULL,
    is_active boolean NOT NULL,
    basket_id bigint NOT NULL,
    promocode_id bigint,
    user_id bigint NOT NULL,
    address_id bigint NOT NULL,
    orderer character varying(255) NOT NULL,
    phone character varying(25) NOT NULL,
    date_delivered date,
    price double precision NOT NULL,
    email character varying(254),
    delivery_price double precision NOT NULL
);


ALTER TABLE public.core_order OWNER TO saidamir;

--
-- Name: core_order_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_order_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_order_id_seq OWNER TO saidamir;

--
-- Name: core_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_order_id_seq OWNED BY public.core_order.id;


--
-- Name: core_product; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_product (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    title character varying(255) NOT NULL,
    description text NOT NULL,
    is_active boolean NOT NULL,
    catalog_id bigint NOT NULL,
    description_ru text,
    description_uz text,
    title_ru character varying(255),
    title_uz character varying(255),
    brand_id bigint,
    description_en text,
    title_en character varying(255),
    price double precision NOT NULL,
    old_price double precision,
    discount smallint,
    available_quantity integer NOT NULL,
    is_slider boolean NOT NULL,
    is_on_sale boolean NOT NULL,
    is_new boolean NOT NULL,
    CONSTRAINT core_product_available_quantity_check CHECK ((available_quantity >= 0)),
    CONSTRAINT core_product_discount_869039f9_check CHECK ((discount >= 0))
);


ALTER TABLE public.core_product OWNER TO saidamir;

--
-- Name: core_product_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_product_id_seq OWNER TO saidamir;

--
-- Name: core_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_product_id_seq OWNED BY public.core_product.id;


--
-- Name: core_productcolor; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_productcolor (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    color character varying(18) NOT NULL,
    title character varying(255),
    title_en character varying(255),
    title_ru character varying(255),
    title_uz character varying(255),
    product_id bigint
);


ALTER TABLE public.core_productcolor OWNER TO saidamir;

--
-- Name: core_productcolor_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_productcolor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_productcolor_id_seq OWNER TO saidamir;

--
-- Name: core_productcolor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_productcolor_id_seq OWNED BY public.core_productcolor.id;


--
-- Name: core_productgroup; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_productgroup (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    title character varying(255) NOT NULL,
    title_en character varying(255),
    title_ru character varying(255),
    title_uz character varying(255)
);


ALTER TABLE public.core_productgroup OWNER TO saidamir;

--
-- Name: core_productgroup_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_productgroup_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_productgroup_id_seq OWNER TO saidamir;

--
-- Name: core_productgroup_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_productgroup_id_seq OWNED BY public.core_productgroup.id;


--
-- Name: core_productimage; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_productimage (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    image character varying(100) NOT NULL,
    is_active boolean NOT NULL,
    product_id bigint NOT NULL,
    color_id bigint
);


ALTER TABLE public.core_productimage OWNER TO saidamir;

--
-- Name: core_productimages_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_productimages_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_productimages_id_seq OWNER TO saidamir;

--
-- Name: core_productimages_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_productimages_id_seq OWNED BY public.core_productimage.id;


--
-- Name: core_productorder; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_productorder (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    quantity integer NOT NULL,
    product_id bigint NOT NULL,
    user_id bigint NOT NULL,
    color_id bigint NOT NULL,
    is_active boolean NOT NULL,
    CONSTRAINT core_productorder_quantity_check CHECK ((quantity >= 0))
);


ALTER TABLE public.core_productorder OWNER TO saidamir;

--
-- Name: core_productorder_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_productorder_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_productorder_id_seq OWNER TO saidamir;

--
-- Name: core_productorder_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_productorder_id_seq OWNED BY public.core_productorder.id;


--
-- Name: core_productorder_product_param; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_productorder_product_param (
    id bigint NOT NULL,
    productorder_id bigint NOT NULL,
    productparam_id bigint NOT NULL
);


ALTER TABLE public.core_productorder_product_param OWNER TO saidamir;

--
-- Name: core_productorder_product_param_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_productorder_product_param_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_productorder_product_param_id_seq OWNER TO saidamir;

--
-- Name: core_productorder_product_param_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_productorder_product_param_id_seq OWNED BY public.core_productorder_product_param.id;


--
-- Name: core_productparam; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_productparam (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    product_id bigint NOT NULL,
    is_important boolean NOT NULL,
    key character varying(255) NOT NULL,
    value character varying(255) NOT NULL,
    group_id bigint,
    key_en character varying(255),
    key_ru character varying(255),
    key_uz character varying(255),
    value_en character varying(255),
    value_ru character varying(255),
    value_uz character varying(255)
);


ALTER TABLE public.core_productparam OWNER TO saidamir;

--
-- Name: core_productparam_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_productparam_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_productparam_id_seq OWNER TO saidamir;

--
-- Name: core_productparam_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_productparam_id_seq OWNED BY public.core_productparam.id;


--
-- Name: core_productprice; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_productprice (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    price double precision NOT NULL,
    available_count integer NOT NULL,
    param_id bigint NOT NULL,
    product_id bigint NOT NULL,
    CONSTRAINT core_productprice_available_count_check CHECK ((available_count >= 0))
);


ALTER TABLE public.core_productprice OWNER TO saidamir;

--
-- Name: core_productprice_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_productprice_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_productprice_id_seq OWNER TO saidamir;

--
-- Name: core_productprice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_productprice_id_seq OWNED BY public.core_productprice.id;


--
-- Name: core_promocode; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_promocode (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    code character varying(255) NOT NULL,
    is_active boolean NOT NULL,
    catalog_id bigint NOT NULL,
    percent double precision NOT NULL
);


ALTER TABLE public.core_promocode OWNER TO saidamir;

--
-- Name: core_promocode_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_promocode_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_promocode_id_seq OWNER TO saidamir;

--
-- Name: core_promocode_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_promocode_id_seq OWNED BY public.core_promocode.id;


--
-- Name: core_rating; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_rating (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    rate double precision NOT NULL,
    product_id bigint NOT NULL,
    user_id bigint NOT NULL,
    review_id bigint
);


ALTER TABLE public.core_rating OWNER TO saidamir;

--
-- Name: core_rating_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_rating_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_rating_id_seq OWNER TO saidamir;

--
-- Name: core_rating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_rating_id_seq OWNED BY public.core_rating.id;


--
-- Name: core_region; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_region (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    name character varying(255) NOT NULL,
    name_en character varying(255),
    name_ru character varying(255),
    name_uz character varying(255),
    is_active boolean NOT NULL
);


ALTER TABLE public.core_region OWNER TO saidamir;

--
-- Name: core_region_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_region_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_region_id_seq OWNER TO saidamir;

--
-- Name: core_region_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_region_id_seq OWNED BY public.core_region.id;


--
-- Name: core_review; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_review (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    comment text NOT NULL,
    "like" character varying(255),
    is_active boolean NOT NULL,
    product_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.core_review OWNER TO saidamir;

--
-- Name: core_review_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_review_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_review_id_seq OWNER TO saidamir;

--
-- Name: core_review_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_review_id_seq OWNED BY public.core_review.id;


--
-- Name: core_reviewimage; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.core_reviewimage (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    photo character varying(100) NOT NULL,
    review_id bigint
);


ALTER TABLE public.core_reviewimage OWNER TO saidamir;

--
-- Name: core_reviewfileattachment_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.core_reviewfileattachment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_reviewfileattachment_id_seq OWNER TO saidamir;

--
-- Name: core_reviewfileattachment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.core_reviewfileattachment_id_seq OWNED BY public.core_reviewimage.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO saidamir;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO saidamir;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO saidamir;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO saidamir;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO saidamir;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO saidamir;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO saidamir;

--
-- Name: paycomuz_transaction; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.paycomuz_transaction (
    id bigint NOT NULL,
    _id character varying(255) NOT NULL,
    request_id integer NOT NULL,
    order_key character varying(255),
    amount numeric(10,2) NOT NULL,
    state integer,
    status character varying(55) NOT NULL,
    perform_datetime character varying(255),
    cancel_datetime character varying(255),
    created_datetime character varying(255),
    reason integer
);


ALTER TABLE public.paycomuz_transaction OWNER TO saidamir;

--
-- Name: paycomuz_transaction_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.paycomuz_transaction_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.paycomuz_transaction_id_seq OWNER TO saidamir;

--
-- Name: paycomuz_transaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.paycomuz_transaction_id_seq OWNED BY public.paycomuz_transaction.id;


--
-- Name: user_address; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.user_address (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    full_name character varying(250) NOT NULL,
    phone character varying(25) NOT NULL,
    zip_code character varying(9) NOT NULL,
    address text NOT NULL,
    user_id bigint NOT NULL,
    region_id bigint
);


ALTER TABLE public.user_address OWNER TO saidamir;

--
-- Name: user_address_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.user_address_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_address_id_seq OWNER TO saidamir;

--
-- Name: user_address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.user_address_id_seq OWNED BY public.user_address.id;


--
-- Name: user_user; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.user_user (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    is_staff boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    user_ident character varying(9) NOT NULL,
    role character varying(255) NOT NULL,
    phone character varying(25) NOT NULL,
    email character varying(254) NOT NULL,
    is_active boolean NOT NULL,
    username character varying(150) NOT NULL
);


ALTER TABLE public.user_user OWNER TO saidamir;

--
-- Name: user_user_groups; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.user_user_groups (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.user_user_groups OWNER TO saidamir;

--
-- Name: user_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.user_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_groups_id_seq OWNER TO saidamir;

--
-- Name: user_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.user_user_groups_id_seq OWNED BY public.user_user_groups.id;


--
-- Name: user_user_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.user_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_id_seq OWNER TO saidamir;

--
-- Name: user_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.user_user_id_seq OWNED BY public.user_user.id;


--
-- Name: user_user_user_permissions; Type: TABLE; Schema: public; Owner: saidamir
--

CREATE TABLE public.user_user_user_permissions (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.user_user_user_permissions OWNER TO saidamir;

--
-- Name: user_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: saidamir
--

CREATE SEQUENCE public.user_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_user_permissions_id_seq OWNER TO saidamir;

--
-- Name: user_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: saidamir
--

ALTER SEQUENCE public.user_user_user_permissions_id_seq OWNED BY public.user_user_user_permissions.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: core_basket id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_basket ALTER COLUMN id SET DEFAULT nextval('public.core_basket_id_seq'::regclass);


--
-- Name: core_basket_products id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_basket_products ALTER COLUMN id SET DEFAULT nextval('public.core_basket_products_id_seq'::regclass);


--
-- Name: core_brand id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_brand ALTER COLUMN id SET DEFAULT nextval('public.core_brand_id_seq'::regclass);


--
-- Name: core_catalog id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_catalog ALTER COLUMN id SET DEFAULT nextval('public.core_catalog_id_seq'::regclass);


--
-- Name: core_comment id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_comment ALTER COLUMN id SET DEFAULT nextval('public.core_comment_id_seq'::regclass);


--
-- Name: core_delivery id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_delivery ALTER COLUMN id SET DEFAULT nextval('public.core_delivery_id_seq'::regclass);


--
-- Name: core_order id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_order ALTER COLUMN id SET DEFAULT nextval('public.core_order_id_seq'::regclass);


--
-- Name: core_product id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_product ALTER COLUMN id SET DEFAULT nextval('public.core_product_id_seq'::regclass);


--
-- Name: core_productcolor id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productcolor ALTER COLUMN id SET DEFAULT nextval('public.core_productcolor_id_seq'::regclass);


--
-- Name: core_productgroup id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productgroup ALTER COLUMN id SET DEFAULT nextval('public.core_productgroup_id_seq'::regclass);


--
-- Name: core_productimage id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productimage ALTER COLUMN id SET DEFAULT nextval('public.core_productimages_id_seq'::regclass);


--
-- Name: core_productorder id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productorder ALTER COLUMN id SET DEFAULT nextval('public.core_productorder_id_seq'::regclass);


--
-- Name: core_productorder_product_param id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productorder_product_param ALTER COLUMN id SET DEFAULT nextval('public.core_productorder_product_param_id_seq'::regclass);


--
-- Name: core_productparam id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productparam ALTER COLUMN id SET DEFAULT nextval('public.core_productparam_id_seq'::regclass);


--
-- Name: core_productprice id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productprice ALTER COLUMN id SET DEFAULT nextval('public.core_productprice_id_seq'::regclass);


--
-- Name: core_promocode id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_promocode ALTER COLUMN id SET DEFAULT nextval('public.core_promocode_id_seq'::regclass);


--
-- Name: core_rating id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_rating ALTER COLUMN id SET DEFAULT nextval('public.core_rating_id_seq'::regclass);


--
-- Name: core_region id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_region ALTER COLUMN id SET DEFAULT nextval('public.core_region_id_seq'::regclass);


--
-- Name: core_review id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_review ALTER COLUMN id SET DEFAULT nextval('public.core_review_id_seq'::regclass);


--
-- Name: core_reviewimage id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_reviewimage ALTER COLUMN id SET DEFAULT nextval('public.core_reviewfileattachment_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: paycomuz_transaction id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.paycomuz_transaction ALTER COLUMN id SET DEFAULT nextval('public.paycomuz_transaction_id_seq'::regclass);


--
-- Name: user_address id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_address ALTER COLUMN id SET DEFAULT nextval('public.user_address_id_seq'::regclass);


--
-- Name: user_user id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user ALTER COLUMN id SET DEFAULT nextval('public.user_user_id_seq'::regclass);


--
-- Name: user_user_groups id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user_groups ALTER COLUMN id SET DEFAULT nextval('public.user_user_groups_id_seq'::regclass);


--
-- Name: user_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.user_user_user_permissions_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add user	6	add_user
22	Can change user	6	change_user
23	Can delete user	6	delete_user
24	Can view user	6	view_user
25	Can add address	7	add_address
26	Can change address	7	change_address
27	Can delete address	7	delete_address
28	Can view address	7	view_address
29	Can add basket	8	add_basket
30	Can change basket	8	change_basket
31	Can delete basket	8	delete_basket
32	Can view basket	8	view_basket
33	Can add catalog	9	add_catalog
34	Can change catalog	9	change_catalog
35	Can delete catalog	9	delete_catalog
36	Can view catalog	9	view_catalog
37	Can add product	10	add_product
38	Can change product	10	change_product
39	Can delete product	10	delete_product
40	Can view product	10	view_product
41	Can add product param	11	add_productparam
42	Can change product param	11	change_productparam
43	Can delete product param	11	delete_productparam
44	Can view product param	11	view_productparam
45	Can add promo code	12	add_promocode
46	Can change promo code	12	change_promocode
47	Can delete promo code	12	delete_promocode
48	Can view promo code	12	view_promocode
49	Can add product price	13	add_productprice
50	Can change product price	13	change_productprice
51	Can delete product price	13	delete_productprice
52	Can view product price	13	view_productprice
53	Can add product order	14	add_productorder
54	Can change product order	14	change_productorder
55	Can delete product order	14	delete_productorder
56	Can view product order	14	view_productorder
57	Can add order	15	add_order
58	Can change order	15	change_order
59	Can delete order	15	delete_order
60	Can view order	15	view_order
61	Can add rating	16	add_rating
62	Can change rating	16	change_rating
63	Can delete rating	16	delete_rating
64	Can view rating	16	view_rating
65	Can add brand	17	add_brand
66	Can change brand	17	change_brand
67	Can delete brand	17	delete_brand
68	Can view brand	17	view_brand
69	Can add product group	18	add_productgroup
70	Can change product group	18	change_productgroup
71	Can delete product group	18	delete_productgroup
72	Can view product group	18	view_productgroup
73	Can add product color	19	add_productcolor
74	Can change product color	19	change_productcolor
75	Can delete product color	19	delete_productcolor
76	Can view product color	19	view_productcolor
77	Can add review	20	add_review
78	Can change review	20	change_review
79	Can delete review	20	delete_review
80	Can view review	20	view_review
81	Can add product image	21	add_productimage
82	Can change product image	21	change_productimage
83	Can delete product image	21	delete_productimage
84	Can view product image	21	view_productimage
85	Can add review image	22	add_reviewimage
86	Can change review image	22	change_reviewimage
87	Can delete review image	22	delete_reviewimage
88	Can view review image	22	view_reviewimage
89	Can add comment	23	add_comment
90	Can change comment	23	change_comment
91	Can delete comment	23	delete_comment
92	Can view comment	23	view_comment
93	Can add transaction	24	add_transaction
94	Can change transaction	24	change_transaction
95	Can delete transaction	24	delete_transaction
96	Can view transaction	24	view_transaction
97	Can add region	25	add_region
98	Can change region	25	change_region
99	Can delete region	25	delete_region
100	Can view region	25	view_region
101	Can add delivery	26	add_delivery
102	Can change delivery	26	change_delivery
103	Can delete delivery	26	delete_delivery
104	Can view delivery	26	view_delivery
\.


--
-- Data for Name: core_basket; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_basket (id, created_at, updated_at, is_active, user_id) FROM stdin;
2	2021-12-11 20:21:52.083824+00	2021-12-11 20:22:02.591305+00	f	1
11	2021-12-17 18:20:04.31625+00	2021-12-17 18:22:32.921267+00	t	1
1	2021-12-11 19:07:31.253348+00	2021-12-16 16:51:46.038725+00	f	1
3	2021-12-11 20:40:59.045701+00	2021-12-16 19:42:04.400856+00	f	1
4	2021-12-16 19:44:48.256847+00	2021-12-16 19:45:09.924238+00	f	1
5	2021-12-16 19:46:58.744263+00	2021-12-16 19:47:44.953616+00	f	1
\.


--
-- Data for Name: core_basket_products; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_basket_products (id, basket_id, productorder_id) FROM stdin;
1	1	1
2	1	2
6	2	3
36	3	14
41	3	16
42	4	17
43	5	18
53	11	26
54	11	27
\.


--
-- Data for Name: core_brand; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_brand (id, created_at, updated_at, title, logo, is_active) FROM stdin;
1	2021-12-11 19:02:02.849885+00	2021-12-11 19:02:02.849911+00	FITLAND	photos/brands/crossfit_Nc41BVq.png	t
\.


--
-- Data for Name: core_catalog; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_catalog (id, created_at, updated_at, title, is_active, lft, rght, tree_id, level, parent_id, title_ru, title_uz, title_en, image) FROM stdin;
1	2021-12-11 19:01:50.474301+00	2021-12-11 19:01:50.474353+00	Футбольный инвентарь	t	1	2	1	0	\N	Футбольный инвентарь	Футбольный инвентарь	Футбольный инвентарь	photos/catalogs/crossfit_02MOkQN.png
\.


--
-- Data for Name: core_comment; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_comment (id, created_at, updated_at, text, is_active, lft, rght, tree_id, level, parent_id, product_id, user_id) FROM stdin;
\.


--
-- Data for Name: core_delivery; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_delivery (id, created_at, updated_at, delivery_price, region_id) FROM stdin;
\.


--
-- Data for Name: core_order; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_order (id, created_at, updated_at, payment_type, order_status, payment_status, is_active, basket_id, promocode_id, user_id, address_id, orderer, phone, date_delivered, price, email, delivery_price) FROM stdin;
3	2021-12-16 16:51:46.048729+00	2021-12-16 16:51:46.048758+00	Payme	Opened	Waiting	t	1	\N	1	3	Amir	998900066077	\N	20300	amir2015@mail.ru	0
4	2021-12-16 19:42:04.411282+00	2021-12-16 19:42:04.41131+00	Cash	Opened	Waiting	t	3	\N	1	3	test test	998909099900	\N	113000	tset@gmail.com	0
5	2021-12-16 19:45:09.932764+00	2021-12-16 19:45:09.932802+00	Cash	Opened	Waiting	t	4	\N	1	3	test test	998909998899	\N	10300	etst@gmail.com	0
6	2021-12-16 19:47:44.96038+00	2021-12-16 19:47:44.960405+00	Cash	Opened	Waiting	t	5	\N	1	3	test test	998900000000	\N	10300	test@gmial.ocm	0
\.


--
-- Data for Name: core_product; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_product (id, created_at, updated_at, title, description, is_active, catalog_id, description_ru, description_uz, title_ru, title_uz, brand_id, description_en, title_en, price, old_price, discount, available_quantity, is_slider, is_on_sale, is_new) FROM stdin;
1	2021-12-11 19:02:31.901109+00	2021-12-11 19:02:31.901136+00	Мяч	Хороший мяч	t	1	Хороший мяч	Хороший мяч	Мяч	Мяч	1	Хороший мяч	Мяч	10000	20000	10	10	f	t	t
2	2021-12-11 19:03:08.696716+00	2021-12-11 19:03:08.696743+00	Футболка	Классная футболка	t	1	Классная футболка	Классная футболка	Футболка	Футболка	1	Классная футболка	Футболка	10000	30000	10	5	f	t	t
\.


--
-- Data for Name: core_productcolor; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_productcolor (id, created_at, updated_at, color, title, title_en, title_ru, title_uz, product_id) FROM stdin;
1	2021-12-11 19:05:29.833766+00	2021-12-16 20:13:54.418597+00	#FFFFFF	белый	\N	белый	\N	1
3	2021-12-16 20:15:58.731244+00	2021-12-16 20:15:58.731276+00	#2CFF22	зеленый	\N	зеленый	\N	1
4	2021-12-16 20:16:07.713486+00	2021-12-16 20:16:07.713515+00	#FF3711	красный	\N	красный	\N	1
2	2021-12-11 19:05:51.085976+00	2021-12-17 18:06:30.543507+00	#3E8DFF	Синий	\N	Синий	\N	2
\.


--
-- Data for Name: core_productgroup; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_productgroup (id, created_at, updated_at, title, title_en, title_ru, title_uz) FROM stdin;
1	2021-12-11 19:03:23.153775+00	2021-12-11 19:03:23.153801+00	Размер	Размер	Размер	Размер
2	2021-12-11 19:04:23.86801+00	2021-12-11 19:04:23.868039+00	Вес	Вес	Вес	Вес
\.


--
-- Data for Name: core_productimage; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_productimage (id, created_at, updated_at, image, is_active, product_id, color_id) FROM stdin;
1	2021-12-11 19:05:35.846594+00	2021-12-11 19:05:35.846621+00	photos/products/crossfit_5Q7tcxJ.png	t	1	1
2	2021-12-11 19:05:57.33815+00	2021-12-11 19:05:57.338179+00	photos/products/crossfit_bJtzfYu.png	t	2	2
\.


--
-- Data for Name: core_productorder; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_productorder (id, created_at, updated_at, quantity, product_id, user_id, color_id, is_active) FROM stdin;
1	2021-12-11 19:07:31.245813+00	2021-12-11 19:07:31.250178+00	1	1	1	1	f
2	2021-12-11 19:07:51.145214+00	2021-12-11 19:12:40.993751+00	1	2	1	2	f
16	2021-12-14 18:20:59.647227+00	2021-12-14 18:20:59.652624+00	10	1	1	1	f
14	2021-12-12 20:09:27.322291+00	2021-12-12 20:09:27.325017+00	1	2	1	1	f
3	2021-12-11 20:21:52.077499+00	2021-12-11 20:21:53.242721+00	1	2	1	2	f
17	2021-12-16 19:44:48.250774+00	2021-12-16 19:44:48.254659+00	1	1	1	1	f
18	2021-12-16 19:46:58.736903+00	2021-12-16 19:46:58.741258+00	1	1	1	1	f
19	2021-12-16 19:48:42.193424+00	2021-12-16 19:48:42.197192+00	1	1	1	1	t
20	2021-12-16 19:54:14.847625+00	2021-12-16 19:54:14.8507+00	1	2	1	1	t
21	2021-12-16 21:07:10.855522+00	2021-12-16 21:07:10.855548+00	10	1	1	1	t
22	2021-12-16 22:15:00.362088+00	2021-12-16 22:15:00.362123+00	10	1	1	1	t
23	2021-12-16 22:27:10.812846+00	2021-12-16 22:27:10.812872+00	10	1	1	1	t
25	2021-12-17 09:23:58.214131+00	2021-12-17 09:24:05.999758+00	4	1	1	1	t
26	2021-12-17 18:20:04.322945+00	2021-12-17 18:20:04.322972+00	1	2	1	2	t
27	2021-12-17 18:20:04.331572+00	2021-12-17 18:22:32.916666+00	3	2	1	2	t
\.


--
-- Data for Name: core_productorder_product_param; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_productorder_product_param (id, productorder_id, productparam_id) FROM stdin;
1	1	1
2	1	3
3	2	5
4	3	5
23	14	5
26	16	1
27	16	3
28	17	1
29	17	3
30	18	1
31	18	3
32	19	1
33	19	3
34	20	5
35	21	1
36	21	3
37	22	1
38	22	3
39	23	1
40	23	3
43	25	2
44	25	3
45	26	5
46	27	6
\.


--
-- Data for Name: core_productparam; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_productparam (id, created_at, updated_at, product_id, is_important, key, value, group_id, key_en, key_ru, key_uz, value_en, value_ru, value_uz) FROM stdin;
1	2021-12-11 19:03:37.664264+00	2021-12-11 19:03:37.664292+00	1	t	Размер	XL	1	\N	Размер	\N	\N	XL	XL
2	2021-12-11 19:03:37.917848+00	2021-12-11 19:04:02.906972+00	1	t	Размер	L	1	\N	Размер	\N	\N	L	L
3	2021-12-11 19:04:31.45849+00	2021-12-11 19:04:31.458527+00	1	t	Вес	10	2	\N	Вес	\N	\N	10	\N
4	2021-12-11 19:04:43.128406+00	2021-12-11 19:04:43.128436+00	1	t	Вес	12	2	\N	Вес	\N	\N	12	\N
5	2021-12-11 19:04:57.959821+00	2021-12-11 19:04:57.959847+00	2	t	Размер	XL	1	\N	Размер	\N	\N	XL	\N
6	2021-12-11 19:05:12.679069+00	2021-12-11 19:05:12.679099+00	2	t	Размер	L	1	\N	Размер	\N	\N	L	\N
\.


--
-- Data for Name: core_productprice; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_productprice (id, created_at, updated_at, price, available_count, param_id, product_id) FROM stdin;
1	2021-12-11 19:06:15.195409+00	2021-12-11 19:06:15.195439+00	1000	10	6	1
2	2021-12-11 19:06:26.245227+00	2021-12-11 19:06:26.245253+00	500	10	5	1
3	2021-12-11 19:06:34.911516+00	2021-12-11 19:06:34.911543+00	50	10	4	1
4	2021-12-11 19:06:42.108867+00	2021-12-11 19:06:42.108905+00	300	20	3	1
5	2021-12-11 19:06:53.112291+00	2021-12-11 19:06:53.112322+00	10000	10	2	2
7	2021-12-16 22:23:16.685222+00	2021-12-16 22:23:16.685253+00	17000	8	1	1
\.


--
-- Data for Name: core_promocode; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_promocode (id, created_at, updated_at, code, is_active, catalog_id, percent) FROM stdin;
\.


--
-- Data for Name: core_rating; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_rating (id, created_at, updated_at, rate, product_id, user_id, review_id) FROM stdin;
\.


--
-- Data for Name: core_region; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_region (id, created_at, updated_at, name, name_en, name_ru, name_uz, is_active) FROM stdin;
3	2012-12-12 00:00:00+00	2012-12-12 00:00:00+00	samarqand	\N	\N	\N	t
\.


--
-- Data for Name: core_review; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_review (id, created_at, updated_at, comment, "like", is_active, product_id, user_id) FROM stdin;
\.


--
-- Data for Name: core_reviewimage; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.core_reviewimage (id, created_at, updated_at, photo, review_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2021-12-11 19:01:50.481752+00	1	Футбольный инвентарь	1	[{"added": {}}]	9	1
2	2021-12-11 19:02:02.853886+00	1	FITLAND	1	[{"added": {}}]	17	1
3	2021-12-11 19:02:31.903973+00	1	Мяч	1	[{"added": {}}]	10	1
4	2021-12-11 19:03:08.698813+00	2	Футболка	1	[{"added": {}}]	10	1
5	2021-12-11 19:03:23.155666+00	1	Размер	1	[{"added": {}}]	18	1
6	2021-12-11 19:03:37.666652+00	1	Размер - XL	1	[{"added": {}}]	11	1
7	2021-12-11 19:03:37.919179+00	2	Размер - XL	1	[{"added": {}}]	11	1
8	2021-12-11 19:03:50.832626+00	2	Размер - XL	2	[{"changed": {"fields": ["Value"]}}]	11	1
9	2021-12-11 19:04:02.908612+00	2	Размер - L	2	[{"changed": {"fields": ["Value", "Value [uz]", "Value [ru]"]}}]	11	1
10	2021-12-11 19:04:23.869891+00	2	Вес	1	[{"added": {}}]	18	1
11	2021-12-11 19:04:31.459909+00	3	Вес - 10	1	[{"added": {}}]	11	1
12	2021-12-11 19:04:43.129771+00	4	Вес - 12	1	[{"added": {}}]	11	1
13	2021-12-11 19:04:57.961275+00	5	Размер - XL	1	[{"added": {}}]	11	1
14	2021-12-11 19:05:12.680538+00	6	Размер - L	1	[{"added": {}}]	11	1
15	2021-12-11 19:05:29.83549+00	1	Белый	1	[{"added": {}}]	19	1
16	2021-12-11 19:05:35.851038+00	1	ProductImage object (1)	1	[{"added": {}}]	21	1
17	2021-12-11 19:05:51.087302+00	2	Синий	1	[{"added": {}}]	19	1
18	2021-12-11 19:05:57.341873+00	2	ProductImage object (2)	1	[{"added": {}}]	21	1
19	2021-12-11 19:06:15.197271+00	1	Мяч - 1000.0	1	[{"added": {}}]	13	1
20	2021-12-11 19:06:26.246377+00	2	Мяч - 500.0	1	[{"added": {}}]	13	1
21	2021-12-11 19:06:34.912551+00	3	Мяч - 50.0	1	[{"added": {}}]	13	1
22	2021-12-11 19:06:42.109912+00	4	Мяч - 300.0	1	[{"added": {}}]	13	1
23	2021-12-11 19:06:53.113581+00	5	Футболка - 10000.0	1	[{"added": {}}]	13	1
24	2021-12-11 19:07:00.463155+00	6	Футболка - 20000.0	1	[{"added": {}}]	13	1
25	2021-12-13 18:52:08.840573+00	1	1	2	[]	6	1
26	2021-12-13 21:32:18.230493+00	2	Order object (2)	2	[{"changed": {"fields": ["Payment type", "Order status"]}}]	15	1
27	2021-12-16 20:13:54.420424+00	1	белый	2	[{"changed": {"fields": ["Product", "Title"]}}]	19	1
28	2021-12-16 20:15:58.733458+00	3	зеленый	1	[{"added": {}}]	19	1
29	2021-12-16 20:16:07.714806+00	4	красный	1	[{"added": {}}]	19	1
30	2021-12-16 22:22:37.119655+00	6	Футболка - 20000.0	3		13	1
31	2021-12-16 22:23:16.687038+00	7	Мяч - 17000.0	1	[{"added": {}}]	13	1
32	2021-12-17 18:06:30.545597+00	2	Синий Футболка	2	[{"changed": {"fields": ["Product", "Title"]}}]	19	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	user	user
7	user	address
8	core	basket
9	core	catalog
10	core	product
11	core	productparam
12	core	promocode
13	core	productprice
14	core	productorder
15	core	order
16	core	rating
17	core	brand
18	core	productgroup
19	core	productcolor
20	core	review
21	core	productimage
22	core	reviewimage
23	core	comment
24	paycomuz	transaction
25	core	region
26	core	delivery
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2021-12-11 08:18:33.76994+00
2	contenttypes	0002_remove_content_type_name	2021-12-11 08:18:33.786262+00
3	auth	0001_initial	2021-12-11 08:18:33.82258+00
4	auth	0002_alter_permission_name_max_length	2021-12-11 08:18:33.831336+00
5	auth	0003_alter_user_email_max_length	2021-12-11 08:18:33.839517+00
6	auth	0004_alter_user_username_opts	2021-12-11 08:18:33.846291+00
7	auth	0005_alter_user_last_login_null	2021-12-11 08:18:33.853716+00
8	auth	0006_require_contenttypes_0002	2021-12-11 08:18:33.856104+00
9	auth	0007_alter_validators_add_error_messages	2021-12-11 08:18:33.86264+00
10	auth	0008_alter_user_username_max_length	2021-12-11 08:18:33.869202+00
11	auth	0009_alter_user_last_name_max_length	2021-12-11 08:18:33.875315+00
12	auth	0010_alter_group_name_max_length	2021-12-11 08:18:33.886647+00
13	auth	0011_update_proxy_permissions	2021-12-11 08:18:33.893307+00
14	auth	0012_alter_user_first_name_max_length	2021-12-11 08:18:33.899871+00
15	user	0001_initial	2021-12-11 08:18:33.93616+00
16	admin	0001_initial	2021-12-11 08:18:34.009448+00
17	admin	0002_logentry_remove_auto_add	2021-12-11 08:18:34.019118+00
18	admin	0003_logentry_add_action_flag_choices	2021-12-11 08:18:34.028568+00
19	core	0001_initial	2021-12-11 08:18:34.21069+00
20	core	0002_productparam_is_important	2021-12-11 08:18:34.222573+00
21	core	0003_comment_rating	2021-12-11 08:18:34.276706+00
22	core	0004_auto_20211130_1954	2021-12-11 08:18:34.315141+00
23	core	0005_auto_20211130_2005	2021-12-11 08:18:34.37443+00
24	core	0006_comment_product	2021-12-11 08:18:34.399003+00
25	core	0004_alter_product_color	2021-12-11 08:18:34.420622+00
26	core	0005_alter_promocode_product	2021-12-11 08:18:34.441318+00
27	core	0007_merge_20211130_2041	2021-12-11 08:18:34.443782+00
28	core	0008_auto_20211130_2041	2021-12-11 08:18:34.490477+00
29	core	0009_auto_20211130_2050	2021-12-11 08:18:34.597532+00
30	core	0010_auto_20211130_2108	2021-12-11 08:18:34.635082+00
31	core	0011_auto_20211130_2111	2021-12-11 08:18:34.669548+00
32	core	0012_auto_20211130_2124	2021-12-11 08:18:34.788744+00
33	core	0013_productorder_color	2021-12-11 08:18:34.816041+00
34	core	0013_alter_order_payment_status	2021-12-11 08:18:34.831985+00
35	core	0014_merge_20211201_0506	2021-12-11 08:18:34.834336+00
36	core	0015_auto_20211201_0606	2021-12-11 08:18:34.898604+00
37	core	0016_auto_20211201_0745	2021-12-11 08:18:34.961849+00
38	core	0017_alter_productparam_is_static	2021-12-11 08:18:34.976133+00
39	core	0018_remove_productparam_is_static	2021-12-11 08:18:34.990081+00
40	core	0019_auto_20211201_0748	2021-12-11 08:18:35.056106+00
41	core	0020_color_color	2021-12-11 08:18:35.064854+00
42	core	0021_auto_20211201_0837	2021-12-11 08:18:35.145116+00
43	core	0022_product_price	2021-12-11 08:18:35.162658+00
44	core	0016_review_reviewfileattachment	2021-12-11 08:18:35.20115+00
45	core	0017_auto_20211201_0839	2021-12-11 08:18:35.252662+00
46	core	0018_rename_reviewfileattachment_reviewattachment	2021-12-11 08:18:35.284169+00
47	core	0022_merge_20211201_0848	2021-12-11 08:18:35.28714+00
48	core	0023_merge_0022_merge_20211201_0848_0022_product_price	2021-12-11 08:18:35.28923+00
49	core	0024_auto_20211201_0901	2021-12-11 08:18:35.367649+00
50	core	0025_auto_20211201_0919	2021-12-11 08:18:35.386964+00
51	core	0026_productorder_is_active	2021-12-11 08:18:35.499619+00
52	core	0027_alter_review_rating	2021-12-11 08:18:35.533211+00
53	core	0028_rename_productimages_productimage	2021-12-11 08:18:35.574179+00
54	core	0029_rename_reviewattachment_reviewimage	2021-12-11 08:18:35.608726+00
55	core	0030_order_date_ordered	2021-12-11 08:18:35.626172+00
56	core	0031_rename_date_ordered_order_date_delivered	2021-12-11 08:18:35.644352+00
57	core	0032_order_price	2021-12-11 08:18:35.667374+00
58	core	0030_alter_productimage_is_active	2021-12-11 08:18:35.683497+00
59	core	0033_merge_20211202_2110	2021-12-11 08:18:35.686027+00
60	core	0034_alter_order_basket	2021-12-11 08:18:35.721986+00
61	core	0033_alter_order_basket	2021-12-11 08:18:35.748174+00
62	core	0035_merge_0033_alter_order_basket_0034_alter_order_basket	2021-12-11 08:18:35.754576+00
63	core	0036_auto_20211203_1545	2021-12-11 08:18:35.799546+00
64	core	0037_alter_productprice_param	2021-12-11 08:18:35.831543+00
65	core	0038_auto_20211203_1903	2021-12-11 08:18:35.867156+00
66	core	0039_alter_productparam_product	2021-12-11 08:18:35.890441+00
67	core	0038_alter_order_order_status	2021-12-11 08:18:35.907187+00
68	core	0040_merge_20211204_0411	2021-12-11 08:18:35.909411+00
69	core	0041_rename_new_price_product_price	2021-12-11 08:18:35.932392+00
70	core	0042_product_discount	2021-12-11 08:18:35.946398+00
71	core	0043_alter_product_old_price	2021-12-11 08:18:35.970996+00
72	core	0042_product_available_quantity	2021-12-11 08:18:35.987196+00
73	core	0044_merge_20211204_1715	2021-12-11 08:18:35.98939+00
74	core	0045_alter_product_available_quantity	2021-12-11 08:18:36.015541+00
75	core	0046_alter_product_available_quantity	2021-12-11 08:18:36.042363+00
76	core	0047_alter_product_available_quantity	2021-12-11 08:18:36.169952+00
77	core	0048_productimage_color	2021-12-11 08:18:36.197489+00
78	core	0049_auto_20211206_0129	2021-12-11 08:18:36.27994+00
79	core	0050_alter_rating_rate	2021-12-11 08:18:36.30257+00
80	core	0051_alter_rating_review	2021-12-11 08:18:36.327038+00
81	core	0052_delete_comment	2021-12-11 08:18:36.332511+00
82	core	0052_auto_20211206_2342	2021-12-11 08:18:36.874975+00
83	core	0053_merge_0052_auto_20211206_2342_0052_delete_comment	2021-12-11 08:18:36.878546+00
84	core	0054_auto_20211207_0141	2021-12-11 08:18:37.290456+00
85	core	0055_product_is_slider	2021-12-11 08:18:37.306365+00
86	core	0056_auto_20211208_2053	2021-12-11 08:18:37.435849+00
87	core	0055_catalog_image	2021-12-11 08:18:37.443435+00
88	core	0057_merge_0055_catalog_image_0056_auto_20211208_2053	2021-12-11 08:18:37.445619+00
89	core	0058_alter_catalog_image	2021-12-11 08:18:37.452256+00
90	core	0059_product_status	2021-12-11 08:18:37.466005+00
91	core	0060_auto_20211209_0003	2021-12-11 08:18:37.493041+00
92	core	0061_comment	2021-12-11 08:18:37.52904+00
93	core	0062_rename_title_comment_text	2021-12-11 08:18:37.553344+00
94	sessions	0001_initial	2021-12-11 08:18:37.564544+00
95	user	0002_auto_20211130_2012	2021-12-11 08:18:37.596712+00
96	user	0003_remove_user_username	2021-12-11 08:18:37.614095+00
97	user	0004_alter_user_managers	2021-12-11 08:18:37.630742+00
98	user	0005_auto_20211130_2245	2021-12-11 08:18:37.669059+00
99	user	0006_alter_user_username	2021-12-11 08:18:37.685702+00
100	user	0007_user_address_en	2021-12-11 08:18:37.703754+00
101	user	0008_alter_user_role	2021-12-11 08:18:37.720879+00
102	user	0009_alter_user_username	2021-12-11 08:18:37.74033+00
103	user	0010_alter_user_username	2021-12-11 08:18:37.757623+00
104	user	0011_auto_20211211_0055	2021-12-11 08:18:37.832008+00
105	user	0012_auto_20211211_0118	2021-12-11 08:18:37.95793+00
106	core	0063_auto_20211212_2111	2021-12-12 18:20:15.551815+00
107	core	0064_alter_rating_review	2021-12-12 18:20:15.584307+00
108	core	0065_productcolor_title	2021-12-12 18:20:15.602945+00
109	core	0066_auto_20211212_2204	2021-12-12 18:20:15.653852+00
110	core	0067_alter_productcolor_product	2021-12-12 18:20:15.707638+00
111	core	0068_alter_order_order_status	2021-12-13 21:28:20.620376+00
112	paycomuz	0001_initial	2021-12-13 21:28:20.640109+00
113	core	0069_alter_productimage_color	2021-12-14 17:38:04.858643+00
114	core	0070_remove_productcolor_product	2021-12-14 17:38:04.892359+00
115	core	0071_productcolor_product	2021-12-14 17:38:04.92491+00
116	core	0072_auto_20211216_2126	2021-12-16 16:46:48.146566+00
117	core	0073_alter_productimage_color	2021-12-16 22:29:07.883609+00
118	core	0074_auto_20211217_1334	2021-12-17 13:22:32.728305+00
119	core	0075_order_delivery_price	2021-12-17 16:45:25.368984+00
120	core	0076_delivery_region	2021-12-17 16:45:25.394435+00
121	core	0077_auto_20211217_1900	2021-12-17 16:45:25.417527+00
122	core	0078_region_is_active	2021-12-17 16:45:25.424839+00
123	core	0079_remove_region_is_active	2021-12-17 16:45:25.43053+00
124	core	0080_region_is_active	2021-12-17 16:45:25.436681+00
125	core	0081_delivery_date_delivered	2021-12-17 16:45:25.442591+00
126	user	0013_address_region	2021-12-17 16:45:25.473747+00
127	core	0082_remove_delivery_date_delivered	2021-12-17 17:46:52.732737+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
xyg2603rzl8rry3v2nhlz5b50zqbvybw	.eJxVjEEOgjAQRe_StWlmKLTUpXvO0EynU0FNSSisjHcXEha6_e-9_1aBtnUMW5UlTEldFarL7xaJn1IOkB5U7rPmuazLFPWh6JNWPcxJXrfT_TsYqY57nZ2x3uYuZ-7JA0ALvgEUQm47YtM3JlqSliUDpsZZcdL7aDwg7xKqzxfbMjfF:1mw7bw:IR4HycWcbPld-mx714W3e3FS4G2q94kugl1w__gUQ0w	2021-12-25 19:00:44.342845+00
kwc5s4xrteriks8i4doq3y7e27gk4on8	.eJxVjEEOgjAQRe_StWlmKLTUpXvO0EynU0FNSSisjHcXEha6_e-9_1aBtnUMW5UlTEldFarL7xaJn1IOkB5U7rPmuazLFPWh6JNWPcxJXrfT_TsYqY57nZ2x3uYuZ-7JA0ALvgEUQm47YtM3JlqSliUDpsZZcdL7aDwg7xKqzxfbMjfF:1mwUsV:G9H9m1bnTcsoKkAqLU5HQINwM4AuCGGTwatqAvE9ZDI	2021-12-26 19:51:23.377647+00
gq2i4t89lhkz9z22s8gismzcql421ags	.eJxVjEEOgjAQRe_StWlmKLTUpXvO0EynU0FNSSisjHcXEha6_e-9_1aBtnUMW5UlTEldFarL7xaJn1IOkB5U7rPmuazLFPWh6JNWPcxJXrfT_TsYqY57nZ2x3uYuZ-7JA0ALvgEUQm47YtM3JlqSliUDpsZZcdL7aDwg7xKqzxfbMjfF:1mwsvQ:dfSoIk1aU-yNhUedSloiDlv5t48LtEVr4dOqXjcKdME	2021-12-27 21:32:00.108039+00
itd7fgg6dgt0c5qrvctdpc9uwinjl3mb	.eJxVjEEOgjAQRe_StWlmKLTUpXvO0EynU0FNSSisjHcXEha6_e-9_1aBtnUMW5UlTEldFarL7xaJn1IOkB5U7rPmuazLFPWh6JNWPcxJXrfT_TsYqY57nZ2x3uYuZ-7JA0ALvgEUQm47YtM3JlqSliUDpsZZcdL7aDwg7xKqzxfbMjfF:1mxx52:Ag1hvVdm7vVuJu0ifX6qFRMnQ0uH3LlWPmbQRR6-u90	2021-12-30 20:10:20.006438+00
i8loz7mspxoiu7b0mjkka0fooagrc83f	.eJxVjEEOgjAQRe_StWlmKLTUpXvO0EynU0FNSSisjHcXEha6_e-9_1aBtnUMW5UlTEldFarL7xaJn1IOkB5U7rPmuazLFPWh6JNWPcxJXrfT_TsYqY57nZ2x3uYuZ-7JA0ALvgEUQm47YtM3JlqSliUDpsZZcdL7aDwg7xKqzxfbMjfF:1myHAZ:WxG1Cvrlz23lxQbDjQ9yOxBBOVW-bw8IDN70-vsVnx4	2021-12-31 17:37:23.430611+00
aaw54qlazh5ajz677gm7exb2n1xuroie	.eJxVjEEOgjAQRe_StWlmKLTUpXvO0EynU0FNSSisjHcXEha6_e-9_1aBtnUMW5UlTEldFarL7xaJn1IOkB5U7rPmuazLFPWh6JNWPcxJXrfT_TsYqY57nZ2x3uYuZ-7JA0ALvgEUQm47YtM3JlqSliUDpsZZcdL7aDwg7xKqzxfbMjfF:1myHcQ:UfOVOjBRiFO_JgAFilnSz142FtIKT65bFe32DZKMElM	2021-12-31 18:06:10.484358+00
\.


--
-- Data for Name: paycomuz_transaction; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.paycomuz_transaction (id, _id, request_id, order_key, amount, state, status, perform_datetime, cancel_datetime, created_datetime, reason) FROM stdin;
\.


--
-- Data for Name: user_address; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.user_address (id, created_at, updated_at, full_name, phone, zip_code, address, user_id, region_id) FROM stdin;
3	2021-12-13 18:05:40.9325+00	2021-12-13 18:05:40.932558+00	test teset test	998111111111	11111111	Tashkent	1	\N
\.


--
-- Data for Name: user_user; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.user_user (id, password, last_login, is_superuser, first_name, last_name, is_staff, date_joined, created_at, updated_at, user_ident, role, phone, email, is_active, username) FROM stdin;
1	pbkdf2_sha256$260000$YtnqiDKVM1MQ6zVojcKcBf$RLiu8ll6EoXAgv990hsRxPQg4prclIqZ4VWFZAllae8=	2021-12-17 18:06:10.480717+00	t	Ali	Amirov	t	2021-12-11 18:59:56+00	2021-12-11 18:59:57.146652+00	2021-12-17 18:20:09.609909+00	217122684	User	998900066077	amir@mail.ru	t	1
-1111	pbkdf2_sha256$260000$3RTsfLnxOC1LOC781tVqkO$eybLaNyvthGYrmfJFvmpx9rHER53PhE/vgwWlI+VYKg=	\N	f			f	2021-12-13 21:28:39.700003+00	2021-12-13 21:28:39.700692+00	2021-12-13 21:28:53.66518+00	254126799	User			t	Paycom
\.


--
-- Data for Name: user_user_groups; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.user_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: user_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: saidamir
--

COPY public.user_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 104, true);


--
-- Name: core_basket_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_basket_id_seq', 11, true);


--
-- Name: core_basket_products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_basket_products_id_seq', 56, true);


--
-- Name: core_brand_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_brand_id_seq', 1, true);


--
-- Name: core_catalog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_catalog_id_seq', 1, true);


--
-- Name: core_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_comment_id_seq', 1, false);


--
-- Name: core_delivery_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_delivery_id_seq', 1, false);


--
-- Name: core_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_order_id_seq', 6, true);


--
-- Name: core_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_product_id_seq', 2, true);


--
-- Name: core_productcolor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_productcolor_id_seq', 4, true);


--
-- Name: core_productgroup_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_productgroup_id_seq', 2, true);


--
-- Name: core_productimages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_productimages_id_seq', 2, true);


--
-- Name: core_productorder_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_productorder_id_seq', 28, true);


--
-- Name: core_productorder_product_param_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_productorder_product_param_id_seq', 48, true);


--
-- Name: core_productparam_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_productparam_id_seq', 6, true);


--
-- Name: core_productprice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_productprice_id_seq', 7, true);


--
-- Name: core_promocode_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_promocode_id_seq', 1, false);


--
-- Name: core_rating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_rating_id_seq', 1, false);


--
-- Name: core_region_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_region_id_seq', 3, true);


--
-- Name: core_review_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_review_id_seq', 1, false);


--
-- Name: core_reviewfileattachment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.core_reviewfileattachment_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 32, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 26, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 127, true);


--
-- Name: paycomuz_transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.paycomuz_transaction_id_seq', 1, false);


--
-- Name: user_address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.user_address_id_seq', 3, true);


--
-- Name: user_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.user_user_groups_id_seq', 1, false);


--
-- Name: user_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.user_user_id_seq', 1, true);


--
-- Name: user_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: saidamir
--

SELECT pg_catalog.setval('public.user_user_user_permissions_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: core_basket core_basket_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_basket
    ADD CONSTRAINT core_basket_pkey PRIMARY KEY (id);


--
-- Name: core_basket_products core_basket_products_basket_id_productorder_id_f5e2a2d8_uniq; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_basket_products
    ADD CONSTRAINT core_basket_products_basket_id_productorder_id_f5e2a2d8_uniq UNIQUE (basket_id, productorder_id);


--
-- Name: core_basket_products core_basket_products_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_basket_products
    ADD CONSTRAINT core_basket_products_pkey PRIMARY KEY (id);


--
-- Name: core_brand core_brand_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_brand
    ADD CONSTRAINT core_brand_pkey PRIMARY KEY (id);


--
-- Name: core_brand core_brand_title_3cddde5c_uniq; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_brand
    ADD CONSTRAINT core_brand_title_3cddde5c_uniq UNIQUE (title);


--
-- Name: core_catalog core_catalog_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_catalog
    ADD CONSTRAINT core_catalog_pkey PRIMARY KEY (id);


--
-- Name: core_catalog core_catalog_title_en_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_catalog
    ADD CONSTRAINT core_catalog_title_en_key UNIQUE (title_en);


--
-- Name: core_catalog core_catalog_title_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_catalog
    ADD CONSTRAINT core_catalog_title_key UNIQUE (title);


--
-- Name: core_catalog core_catalog_title_ru_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_catalog
    ADD CONSTRAINT core_catalog_title_ru_key UNIQUE (title_ru);


--
-- Name: core_catalog core_catalog_title_uz_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_catalog
    ADD CONSTRAINT core_catalog_title_uz_key UNIQUE (title_uz);


--
-- Name: core_comment core_comment_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_comment
    ADD CONSTRAINT core_comment_pkey PRIMARY KEY (id);


--
-- Name: core_delivery core_delivery_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_delivery
    ADD CONSTRAINT core_delivery_pkey PRIMARY KEY (id);


--
-- Name: core_delivery core_delivery_region_id_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_delivery
    ADD CONSTRAINT core_delivery_region_id_key UNIQUE (region_id);


--
-- Name: core_order core_order_basket_id_2640edd1_uniq; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_order
    ADD CONSTRAINT core_order_basket_id_2640edd1_uniq UNIQUE (basket_id);


--
-- Name: core_order core_order_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_order
    ADD CONSTRAINT core_order_pkey PRIMARY KEY (id);


--
-- Name: core_product core_product_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_product
    ADD CONSTRAINT core_product_pkey PRIMARY KEY (id);


--
-- Name: core_productcolor core_productcolor_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productcolor
    ADD CONSTRAINT core_productcolor_pkey PRIMARY KEY (id);


--
-- Name: core_productgroup core_productgroup_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productgroup
    ADD CONSTRAINT core_productgroup_pkey PRIMARY KEY (id);


--
-- Name: core_productgroup core_productgroup_title_en_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productgroup
    ADD CONSTRAINT core_productgroup_title_en_key UNIQUE (title_en);


--
-- Name: core_productgroup core_productgroup_title_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productgroup
    ADD CONSTRAINT core_productgroup_title_key UNIQUE (title);


--
-- Name: core_productgroup core_productgroup_title_ru_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productgroup
    ADD CONSTRAINT core_productgroup_title_ru_key UNIQUE (title_ru);


--
-- Name: core_productgroup core_productgroup_title_uz_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productgroup
    ADD CONSTRAINT core_productgroup_title_uz_key UNIQUE (title_uz);


--
-- Name: core_productimage core_productimages_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productimage
    ADD CONSTRAINT core_productimages_pkey PRIMARY KEY (id);


--
-- Name: core_productorder core_productorder_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productorder
    ADD CONSTRAINT core_productorder_pkey PRIMARY KEY (id);


--
-- Name: core_productorder_product_param core_productorder_produc_productorder_id_productp_091d1fd3_uniq; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productorder_product_param
    ADD CONSTRAINT core_productorder_produc_productorder_id_productp_091d1fd3_uniq UNIQUE (productorder_id, productparam_id);


--
-- Name: core_productorder_product_param core_productorder_product_param_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productorder_product_param
    ADD CONSTRAINT core_productorder_product_param_pkey PRIMARY KEY (id);


--
-- Name: core_productparam core_productparam_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productparam
    ADD CONSTRAINT core_productparam_pkey PRIMARY KEY (id);


--
-- Name: core_productprice core_productprice_param_id_937f2a93_uniq; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productprice
    ADD CONSTRAINT core_productprice_param_id_937f2a93_uniq UNIQUE (param_id);


--
-- Name: core_productprice core_productprice_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productprice
    ADD CONSTRAINT core_productprice_pkey PRIMARY KEY (id);


--
-- Name: core_promocode core_promocode_code_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_promocode
    ADD CONSTRAINT core_promocode_code_key UNIQUE (code);


--
-- Name: core_promocode core_promocode_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_promocode
    ADD CONSTRAINT core_promocode_pkey PRIMARY KEY (id);


--
-- Name: core_rating core_rating_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_rating
    ADD CONSTRAINT core_rating_pkey PRIMARY KEY (id);


--
-- Name: core_rating core_rating_review_id_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_rating
    ADD CONSTRAINT core_rating_review_id_key UNIQUE (review_id);


--
-- Name: core_region core_region_name_en_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_region
    ADD CONSTRAINT core_region_name_en_key UNIQUE (name_en);


--
-- Name: core_region core_region_name_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_region
    ADD CONSTRAINT core_region_name_key UNIQUE (name);


--
-- Name: core_region core_region_name_ru_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_region
    ADD CONSTRAINT core_region_name_ru_key UNIQUE (name_ru);


--
-- Name: core_region core_region_name_uz_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_region
    ADD CONSTRAINT core_region_name_uz_key UNIQUE (name_uz);


--
-- Name: core_region core_region_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_region
    ADD CONSTRAINT core_region_pkey PRIMARY KEY (id);


--
-- Name: core_review core_review_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_review
    ADD CONSTRAINT core_review_pkey PRIMARY KEY (id);


--
-- Name: core_reviewimage core_reviewfileattachment_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_reviewimage
    ADD CONSTRAINT core_reviewfileattachment_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: paycomuz_transaction paycomuz_transaction_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.paycomuz_transaction
    ADD CONSTRAINT paycomuz_transaction_pkey PRIMARY KEY (id);


--
-- Name: user_address user_address_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_address
    ADD CONSTRAINT user_address_pkey PRIMARY KEY (id);


--
-- Name: user_user user_user_email_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_email_key UNIQUE (email);


--
-- Name: user_user_groups user_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_pkey PRIMARY KEY (id);


--
-- Name: user_user_groups user_user_groups_user_id_group_id_bb60391f_uniq; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_user_id_group_id_bb60391f_uniq UNIQUE (user_id, group_id);


--
-- Name: user_user user_user_phone_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_phone_key UNIQUE (phone);


--
-- Name: user_user user_user_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_pkey PRIMARY KEY (id);


--
-- Name: user_user user_user_user_ident_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_user_ident_key UNIQUE (user_ident);


--
-- Name: user_user_user_permissions user_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: user_user_user_permissions user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq UNIQUE (user_id, permission_id);


--
-- Name: user_user user_user_username_key; Type: CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_username_key UNIQUE (username);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: core_basket_products_basket_id_e375332f; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_basket_products_basket_id_e375332f ON public.core_basket_products USING btree (basket_id);


--
-- Name: core_basket_products_productorder_id_56a6ffd7; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_basket_products_productorder_id_56a6ffd7 ON public.core_basket_products USING btree (productorder_id);


--
-- Name: core_basket_user_id_69198906; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_basket_user_id_69198906 ON public.core_basket USING btree (user_id);


--
-- Name: core_brand_title_3cddde5c_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_brand_title_3cddde5c_like ON public.core_brand USING btree (title varchar_pattern_ops);


--
-- Name: core_catalog_parent_id_95f43af4; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_catalog_parent_id_95f43af4 ON public.core_catalog USING btree (parent_id);


--
-- Name: core_catalog_title_7d912f1d_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_catalog_title_7d912f1d_like ON public.core_catalog USING btree (title varchar_pattern_ops);


--
-- Name: core_catalog_title_en_889d6efe_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_catalog_title_en_889d6efe_like ON public.core_catalog USING btree (title_en varchar_pattern_ops);


--
-- Name: core_catalog_title_ru_aa758e99_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_catalog_title_ru_aa758e99_like ON public.core_catalog USING btree (title_ru varchar_pattern_ops);


--
-- Name: core_catalog_title_uz_25d185e0_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_catalog_title_uz_25d185e0_like ON public.core_catalog USING btree (title_uz varchar_pattern_ops);


--
-- Name: core_catalog_tree_id_cfc0c363; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_catalog_tree_id_cfc0c363 ON public.core_catalog USING btree (tree_id);


--
-- Name: core_comment_parent_id_1b4ed377; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_comment_parent_id_1b4ed377 ON public.core_comment USING btree (parent_id);


--
-- Name: core_comment_product_id_ddb6e5eb; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_comment_product_id_ddb6e5eb ON public.core_comment USING btree (product_id);


--
-- Name: core_comment_tree_id_5acce8cf; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_comment_tree_id_5acce8cf ON public.core_comment USING btree (tree_id);


--
-- Name: core_comment_user_id_a9a9430c; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_comment_user_id_a9a9430c ON public.core_comment USING btree (user_id);


--
-- Name: core_order_address_id_caf8cd86; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_order_address_id_caf8cd86 ON public.core_order USING btree (address_id);


--
-- Name: core_order_promocode_id_b2725d23; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_order_promocode_id_b2725d23 ON public.core_order USING btree (promocode_id);


--
-- Name: core_order_user_id_b03bbffd; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_order_user_id_b03bbffd ON public.core_order USING btree (user_id);


--
-- Name: core_product_brand_id_a97b95f2; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_product_brand_id_a97b95f2 ON public.core_product USING btree (brand_id);


--
-- Name: core_product_catalog_id_caa929fe; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_product_catalog_id_caa929fe ON public.core_product USING btree (catalog_id);


--
-- Name: core_productcolor_product_id_671e3d97; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productcolor_product_id_671e3d97 ON public.core_productcolor USING btree (product_id);


--
-- Name: core_productgroup_title_384b78d2_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productgroup_title_384b78d2_like ON public.core_productgroup USING btree (title varchar_pattern_ops);


--
-- Name: core_productgroup_title_en_78df0ccb_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productgroup_title_en_78df0ccb_like ON public.core_productgroup USING btree (title_en varchar_pattern_ops);


--
-- Name: core_productgroup_title_ru_092bccc5_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productgroup_title_ru_092bccc5_like ON public.core_productgroup USING btree (title_ru varchar_pattern_ops);


--
-- Name: core_productgroup_title_uz_06264682_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productgroup_title_uz_06264682_like ON public.core_productgroup USING btree (title_uz varchar_pattern_ops);


--
-- Name: core_productimage_color_id_7ddf6406; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productimage_color_id_7ddf6406 ON public.core_productimage USING btree (color_id);


--
-- Name: core_productimages_product_id_64dfbcf1; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productimages_product_id_64dfbcf1 ON public.core_productimage USING btree (product_id);


--
-- Name: core_productorder_color_id_d7959a5d; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productorder_color_id_d7959a5d ON public.core_productorder USING btree (color_id);


--
-- Name: core_productorder_product_id_aa75e690; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productorder_product_id_aa75e690 ON public.core_productorder USING btree (product_id);


--
-- Name: core_productorder_product_param_productorder_id_b9e1763d; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productorder_product_param_productorder_id_b9e1763d ON public.core_productorder_product_param USING btree (productorder_id);


--
-- Name: core_productorder_product_param_productparam_id_62502944; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productorder_product_param_productparam_id_62502944 ON public.core_productorder_product_param USING btree (productparam_id);


--
-- Name: core_productorder_user_id_abb9dd3d; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productorder_user_id_abb9dd3d ON public.core_productorder USING btree (user_id);


--
-- Name: core_productparam_group_id_f0917ec6; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productparam_group_id_f0917ec6 ON public.core_productparam USING btree (group_id);


--
-- Name: core_productparam_product_id_6deb7dec; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productparam_product_id_6deb7dec ON public.core_productparam USING btree (product_id);


--
-- Name: core_productprice_product_id_89d7e82f; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_productprice_product_id_89d7e82f ON public.core_productprice USING btree (product_id);


--
-- Name: core_promocode_catalog_id_90c76a57; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_promocode_catalog_id_90c76a57 ON public.core_promocode USING btree (catalog_id);


--
-- Name: core_promocode_code_30658daa_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_promocode_code_30658daa_like ON public.core_promocode USING btree (code varchar_pattern_ops);


--
-- Name: core_rating_product_id_ac4401f1; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_rating_product_id_ac4401f1 ON public.core_rating USING btree (product_id);


--
-- Name: core_rating_user_id_0c12e4af; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_rating_user_id_0c12e4af ON public.core_rating USING btree (user_id);


--
-- Name: core_region_name_c4edcc3c_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_region_name_c4edcc3c_like ON public.core_region USING btree (name varchar_pattern_ops);


--
-- Name: core_region_name_en_260f02bc_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_region_name_en_260f02bc_like ON public.core_region USING btree (name_en varchar_pattern_ops);


--
-- Name: core_region_name_ru_5902a92f_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_region_name_ru_5902a92f_like ON public.core_region USING btree (name_ru varchar_pattern_ops);


--
-- Name: core_region_name_uz_12471bdd_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_region_name_uz_12471bdd_like ON public.core_region USING btree (name_uz varchar_pattern_ops);


--
-- Name: core_review_product_id_27ba91fa; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_review_product_id_27ba91fa ON public.core_review USING btree (product_id);


--
-- Name: core_review_user_id_b6106194; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_review_user_id_b6106194 ON public.core_review USING btree (user_id);


--
-- Name: core_reviewfileattachment_review_id_795b0206; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX core_reviewfileattachment_review_id_795b0206 ON public.core_reviewimage USING btree (review_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: user_address_region_id_683afef7; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX user_address_region_id_683afef7 ON public.user_address USING btree (region_id);


--
-- Name: user_address_user_id_64deb2c7; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX user_address_user_id_64deb2c7 ON public.user_address USING btree (user_id);


--
-- Name: user_user_email_1c6f3d1a_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX user_user_email_1c6f3d1a_like ON public.user_user USING btree (email varchar_pattern_ops);


--
-- Name: user_user_groups_group_id_c57f13c0; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX user_user_groups_group_id_c57f13c0 ON public.user_user_groups USING btree (group_id);


--
-- Name: user_user_groups_user_id_13f9a20d; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX user_user_groups_user_id_13f9a20d ON public.user_user_groups USING btree (user_id);


--
-- Name: user_user_phone_9279a142_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX user_user_phone_9279a142_like ON public.user_user USING btree (phone varchar_pattern_ops);


--
-- Name: user_user_user_ident_2048acba_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX user_user_user_ident_2048acba_like ON public.user_user USING btree (user_ident varchar_pattern_ops);


--
-- Name: user_user_user_permissions_permission_id_ce49d4de; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX user_user_user_permissions_permission_id_ce49d4de ON public.user_user_user_permissions USING btree (permission_id);


--
-- Name: user_user_user_permissions_user_id_31782f58; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX user_user_user_permissions_user_id_31782f58 ON public.user_user_user_permissions USING btree (user_id);


--
-- Name: user_user_username_e2bdfe0c_like; Type: INDEX; Schema: public; Owner: saidamir
--

CREATE INDEX user_user_username_e2bdfe0c_like ON public.user_user USING btree (username varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_basket_products core_basket_products_basket_id_e375332f_fk_core_basket_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_basket_products
    ADD CONSTRAINT core_basket_products_basket_id_e375332f_fk_core_basket_id FOREIGN KEY (basket_id) REFERENCES public.core_basket(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_basket_products core_basket_products_productorder_id_56a6ffd7_fk_core_prod; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_basket_products
    ADD CONSTRAINT core_basket_products_productorder_id_56a6ffd7_fk_core_prod FOREIGN KEY (productorder_id) REFERENCES public.core_productorder(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_basket core_basket_user_id_69198906_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_basket
    ADD CONSTRAINT core_basket_user_id_69198906_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_catalog core_catalog_parent_id_95f43af4_fk_core_catalog_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_catalog
    ADD CONSTRAINT core_catalog_parent_id_95f43af4_fk_core_catalog_id FOREIGN KEY (parent_id) REFERENCES public.core_catalog(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_comment core_comment_parent_id_1b4ed377_fk_core_comment_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_comment
    ADD CONSTRAINT core_comment_parent_id_1b4ed377_fk_core_comment_id FOREIGN KEY (parent_id) REFERENCES public.core_comment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_comment core_comment_product_id_ddb6e5eb_fk_core_product_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_comment
    ADD CONSTRAINT core_comment_product_id_ddb6e5eb_fk_core_product_id FOREIGN KEY (product_id) REFERENCES public.core_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_comment core_comment_user_id_a9a9430c_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_comment
    ADD CONSTRAINT core_comment_user_id_a9a9430c_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_delivery core_delivery_region_id_fdf6b13b_fk_core_region_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_delivery
    ADD CONSTRAINT core_delivery_region_id_fdf6b13b_fk_core_region_id FOREIGN KEY (region_id) REFERENCES public.core_region(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_order core_order_address_id_caf8cd86_fk_user_address_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_order
    ADD CONSTRAINT core_order_address_id_caf8cd86_fk_user_address_id FOREIGN KEY (address_id) REFERENCES public.user_address(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_order core_order_basket_id_2640edd1_fk_core_basket_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_order
    ADD CONSTRAINT core_order_basket_id_2640edd1_fk_core_basket_id FOREIGN KEY (basket_id) REFERENCES public.core_basket(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_order core_order_promocode_id_b2725d23_fk_core_promocode_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_order
    ADD CONSTRAINT core_order_promocode_id_b2725d23_fk_core_promocode_id FOREIGN KEY (promocode_id) REFERENCES public.core_promocode(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_order core_order_user_id_b03bbffd_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_order
    ADD CONSTRAINT core_order_user_id_b03bbffd_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_product core_product_brand_id_a97b95f2_fk_core_brand_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_product
    ADD CONSTRAINT core_product_brand_id_a97b95f2_fk_core_brand_id FOREIGN KEY (brand_id) REFERENCES public.core_brand(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_product core_product_catalog_id_caa929fe_fk_core_catalog_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_product
    ADD CONSTRAINT core_product_catalog_id_caa929fe_fk_core_catalog_id FOREIGN KEY (catalog_id) REFERENCES public.core_catalog(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_productcolor core_productcolor_product_id_671e3d97_fk_core_product_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productcolor
    ADD CONSTRAINT core_productcolor_product_id_671e3d97_fk_core_product_id FOREIGN KEY (product_id) REFERENCES public.core_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_productimage core_productimage_color_id_7ddf6406_fk_core_productcolor_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productimage
    ADD CONSTRAINT core_productimage_color_id_7ddf6406_fk_core_productcolor_id FOREIGN KEY (color_id) REFERENCES public.core_productcolor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_productimage core_productimages_product_id_64dfbcf1_fk_core_product_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productimage
    ADD CONSTRAINT core_productimages_product_id_64dfbcf1_fk_core_product_id FOREIGN KEY (product_id) REFERENCES public.core_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_productorder core_productorder_color_id_d7959a5d_fk_core_productcolor_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productorder
    ADD CONSTRAINT core_productorder_color_id_d7959a5d_fk_core_productcolor_id FOREIGN KEY (color_id) REFERENCES public.core_productcolor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_productorder_product_param core_productorder_pr_productorder_id_b9e1763d_fk_core_prod; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productorder_product_param
    ADD CONSTRAINT core_productorder_pr_productorder_id_b9e1763d_fk_core_prod FOREIGN KEY (productorder_id) REFERENCES public.core_productorder(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_productorder_product_param core_productorder_pr_productparam_id_62502944_fk_core_prod; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productorder_product_param
    ADD CONSTRAINT core_productorder_pr_productparam_id_62502944_fk_core_prod FOREIGN KEY (productparam_id) REFERENCES public.core_productparam(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_productorder core_productorder_product_id_aa75e690_fk_core_product_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productorder
    ADD CONSTRAINT core_productorder_product_id_aa75e690_fk_core_product_id FOREIGN KEY (product_id) REFERENCES public.core_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_productorder core_productorder_user_id_abb9dd3d_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productorder
    ADD CONSTRAINT core_productorder_user_id_abb9dd3d_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_productparam core_productparam_group_id_f0917ec6_fk_core_productgroup_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productparam
    ADD CONSTRAINT core_productparam_group_id_f0917ec6_fk_core_productgroup_id FOREIGN KEY (group_id) REFERENCES public.core_productgroup(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_productparam core_productparam_product_id_6deb7dec_fk_core_product_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productparam
    ADD CONSTRAINT core_productparam_product_id_6deb7dec_fk_core_product_id FOREIGN KEY (product_id) REFERENCES public.core_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_productprice core_productprice_param_id_937f2a93_fk_core_productparam_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productprice
    ADD CONSTRAINT core_productprice_param_id_937f2a93_fk_core_productparam_id FOREIGN KEY (param_id) REFERENCES public.core_productparam(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_productprice core_productprice_product_id_89d7e82f_fk_core_product_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_productprice
    ADD CONSTRAINT core_productprice_product_id_89d7e82f_fk_core_product_id FOREIGN KEY (product_id) REFERENCES public.core_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_promocode core_promocode_catalog_id_90c76a57_fk_core_catalog_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_promocode
    ADD CONSTRAINT core_promocode_catalog_id_90c76a57_fk_core_catalog_id FOREIGN KEY (catalog_id) REFERENCES public.core_catalog(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_rating core_rating_product_id_ac4401f1_fk_core_product_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_rating
    ADD CONSTRAINT core_rating_product_id_ac4401f1_fk_core_product_id FOREIGN KEY (product_id) REFERENCES public.core_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_rating core_rating_review_id_eb72ee12_fk_core_review_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_rating
    ADD CONSTRAINT core_rating_review_id_eb72ee12_fk_core_review_id FOREIGN KEY (review_id) REFERENCES public.core_review(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_rating core_rating_user_id_0c12e4af_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_rating
    ADD CONSTRAINT core_rating_user_id_0c12e4af_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_review core_review_product_id_27ba91fa_fk_core_product_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_review
    ADD CONSTRAINT core_review_product_id_27ba91fa_fk_core_product_id FOREIGN KEY (product_id) REFERENCES public.core_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_review core_review_user_id_b6106194_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_review
    ADD CONSTRAINT core_review_user_id_b6106194_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_reviewimage core_reviewfileattachment_review_id_795b0206_fk_core_review_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.core_reviewimage
    ADD CONSTRAINT core_reviewfileattachment_review_id_795b0206_fk_core_review_id FOREIGN KEY (review_id) REFERENCES public.core_review(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_address user_address_region_id_683afef7_fk_core_region_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_address
    ADD CONSTRAINT user_address_region_id_683afef7_fk_core_region_id FOREIGN KEY (region_id) REFERENCES public.core_region(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_address user_address_user_id_64deb2c7_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_address
    ADD CONSTRAINT user_address_user_id_64deb2c7_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_groups user_user_groups_group_id_c57f13c0_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_group_id_c57f13c0_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_groups user_user_groups_user_id_13f9a20d_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_user_id_13f9a20d_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_user_permissions user_user_user_permi_permission_id_ce49d4de_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permi_permission_id_ce49d4de_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_user_permissions user_user_user_permissions_user_id_31782f58_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: saidamir
--

ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permissions_user_id_31782f58_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg110+1)
-- Dumped by pg_dump version 14.1 (Debian 14.1-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE postgres;
--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: saidamir
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE postgres OWNER TO saidamir;

\connect postgres

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: saidamir
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

