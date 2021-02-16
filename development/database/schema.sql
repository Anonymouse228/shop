CREATE TABLE "Product" (
	"id" serial NOT NULL UNIQUE,
	"title" varchar(255) NOT NULL,
	"price" integer NOT NULL,
	"category" integer NOT NULL,
	"description" TEXT NOT NULL,
	"manufacturer" integer NOT NULL,
	"visible" BOOLEAN NOT NULL DEFAULT 'True',
	"amount" integer NOT NULL,
	"created_at" DATETIME NOT NULL,
	"updated_at" DATETIME,
	CONSTRAINT "Product_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Category" (
	"id" serial NOT NULL UNIQUE,
	"name" varchar(255) NOT NULL UNIQUE,
	"parent" integer,
	"created_at" DATETIME NOT NULL,
	"updated_at" DATETIME,
	CONSTRAINT "Category_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Manufacturer" (
	"id" serial NOT NULL UNIQUE,
	"name" varchar(255) NOT NULL,
	"created_at" DATETIME NOT NULL,
	"updated_at" DATETIME,
	CONSTRAINT "Manufacturer_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "User" (
	"id" serial NOT NULL UNIQUE,
	"name" varchar(255) NOT NULL,
	"email" varchar(255) NOT NULL UNIQUE,
	"password" varchar(255) NOT NULL,
	"created_at" DATETIME NOT NULL,
	"updated_at" DATETIME,
	CONSTRAINT "User_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Review" (
	"id" serial NOT NULL UNIQUE,
	"product" integer NOT NULL,
	"user" integer NOT NULL,
	"rating" integer NOT NULL,
	"title" varchar(255) NOT NULL,
	"description" TEXT NOT NULL,
	"created_at" DATETIME NOT NULL,
	"updated_at" DATETIME,
	CONSTRAINT "Review_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Cart" (
	"id" serial NOT NULL UNIQUE,
	"price" serial NOT NULL,
	"user" integer NOT NULL,
	"created_at" DATETIME NOT NULL,
	"updated_at" DATETIME,
	CONSTRAINT "Cart_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Order" (
	"id" serial NOT NULL UNIQUE,
	"user" integer NOT NULL,
	"price" integer NOT NULL,
	"discounted_price" integer,
	"created_at" DATETIME NOT NULL,
	"updated_at" DATETIME,
	CONSTRAINT "Order_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Discount" (
	"id" serial NOT NULL,
	"code" varchar(255) NOT NULL,
	"value" integer NOT NULL,
	"is_active" BOOLEAN NOT NULL DEFAULT 'False',
	"available_to" DATETIME NOT NULL,
	"count" integer NOT NULL,
	"created_at" DATETIME NOT NULL,
	"updated_at" DATETIME,
	CONSTRAINT "Discount_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "discount_user" (
	"user_id" integer NOT NULL UNIQUE,
	"discount_id" integer NOT NULL UNIQUE
) WITH (
  OIDS=FALSE
);



CREATE TABLE "order_products" (
	"id" serial NOT NULL,
	"product_id" integer NOT NULL,
	"order_id" integer NOT NULL,
	"price_per_item" integer NOT NULL,
	"count" integer NOT NULL,
	"created_at" DATETIME NOT NULL,
	"updated_at" DATETIME,
	CONSTRAINT "order_products_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "cart_products" (
	"id" serial NOT NULL,
	"product_id" integer NOT NULL,
	"cart_id" integer NOT NULL,
	"price_per_item" integer NOT NULL,
	"count" integer NOT NULL,
	"created_at" DATETIME NOT NULL,
	"updated_at" DATETIME,
	CONSTRAINT "cart_products_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "Product" ADD CONSTRAINT "Product_fk0" FOREIGN KEY ("category") REFERENCES "Category"("id");
ALTER TABLE "Product" ADD CONSTRAINT "Product_fk1" FOREIGN KEY ("manufacturer") REFERENCES "Manufacturer"("id");

ALTER TABLE "Category" ADD CONSTRAINT "Category_fk0" FOREIGN KEY ("parent") REFERENCES "Category"("id");



ALTER TABLE "Review" ADD CONSTRAINT "Review_fk0" FOREIGN KEY ("product") REFERENCES "Product"("id");
ALTER TABLE "Review" ADD CONSTRAINT "Review_fk1" FOREIGN KEY ("user") REFERENCES "User"("id");

ALTER TABLE "Cart" ADD CONSTRAINT "Cart_fk0" FOREIGN KEY ("user") REFERENCES "User"("id");

ALTER TABLE "Order" ADD CONSTRAINT "Order_fk0" FOREIGN KEY ("user") REFERENCES "User"("id");


ALTER TABLE "discount_user" ADD CONSTRAINT "discount_user_fk0" FOREIGN KEY ("user_id") REFERENCES "User"("id");
ALTER TABLE "discount_user" ADD CONSTRAINT "discount_user_fk1" FOREIGN KEY ("discount_id") REFERENCES "Discount"("id");

ALTER TABLE "order_products" ADD CONSTRAINT "order_products_fk0" FOREIGN KEY ("product_id") REFERENCES "Product"("id");
ALTER TABLE "order_products" ADD CONSTRAINT "order_products_fk1" FOREIGN KEY ("order_id") REFERENCES "Order"("id");

ALTER TABLE "cart_products" ADD CONSTRAINT "cart_products_fk0" FOREIGN KEY ("product_id") REFERENCES "Product"("id");
ALTER TABLE "cart_products" ADD CONSTRAINT "cart_products_fk1" FOREIGN KEY ("cart_id") REFERENCES "Cart"("id");

