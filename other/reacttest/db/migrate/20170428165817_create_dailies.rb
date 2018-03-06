class CreateDailies < ActiveRecord::Migration[5.0]
  def change
    create_table :dailies do |t|
      t.string :name
      t.text :description
      t.integer :whatever

      t.timestamps
    end
  end
end
